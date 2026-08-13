"""
Application Programming CCGC 5003  Summer 2026
Humber College Institute of Technology and Advanced Learning
Waypoint - Web App
Part 6/7/8 - Database, Relationships, and Hardening (WP-605, WP-705, WP-801)
Developed by (IATIDEL AKIK N10038365)

Description:
This module defines the trails app's views. catalog() shows every
open trail across all parks. trails_by_park() demonstrates a
cross-relation query (WP-705): given a park's id from the URL, it
filters trails using park__id, reaching across the ForeignKey from
Trail to Park. trail_detail() shows one trail's full details, and
automatically returns a 404 if no trail with that id exists.

Functions:
    catalog(request)                 : queries all open trails from the
                                        database, ordered by distance,
                                        and renders catalog.html
    trails_by_park(request, park_id) : queries open trails belonging
                                        to one specific park (cross-relation
                                        query via park__id), renders the
                                        same catalog.html template
    trail_detail(request, trail_id)  : shows one trail's details, or a
                                        404 if no matching trail exists
"""

from django.shortcuts import render, get_object_or_404
from .models import Trail


def catalog(request):
    """
    Renders the public trail catalog from the database - only trails
    where is_open is True, ordered by distance_km ascending.
    Parameters:
        request (HttpRequest): the incoming request object
    Returns:
        HttpResponse: the rendered catalog page, using real Trail
                       model instances instead of hardcoded dicts
    """
    # .filter() narrows the query to only open trails - closed
    # trails are never included, satisfying the acceptance criteria
    trails = Trail.objects.filter(is_open=True).order_by("distance_km")

    context = {"trails": trails}
    return render(request, "catalog.html", context)


def trails_by_park(request, park_id):
    """
    Shows all trails belonging to a specific park (cross-relation
    query, WP-705). Only open trails are shown, ordered by distance -
    consistent with the main catalog's behavior.
    Parameters:
        request (HttpRequest): the incoming request object
        park_id (int): the id of the park to show trails for
    Returns:
        HttpResponse: the rendered catalog page, filtered to one park
    """
    # Cross-relation query: filter Trail by its park's id, and also
    # require is_open=True, same rule as the main catalog
    trails = Trail.objects.filter(park__id=park_id, is_open=True).order_by("distance_km")

    context = {"trails": trails}
    return render(request, "catalog.html", context)


def trail_detail(request, trail_id):
    """
    Shows a single trail's details. Returns a 404 if no trail with
    that id exists.
    Parameters:
        request (HttpRequest): the incoming request object
        trail_id (int): the id of the trail to show
    Returns:
        HttpResponse: the rendered detail page, or a 404 if not found
    """
    # get_object_or_404 fetches the trail, or automatically raises
    # Http404 if no matching row exists - no manual if/else needed
    trail = get_object_or_404(Trail, id=trail_id)

    context = {"trail": trail}
    return render(request, "trail_detail.html", context)
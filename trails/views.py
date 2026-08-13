"""
Application Programming CCGC 5003  Summer 2026
Humber College Institute of Technology and Advanced Learning
Waypoint - Web App
Part 6/7 - The Database and Relationships (WP-605, WP-705)
Developed by (IATIDEL AKIK N10038365)

Description:
This module defines the trails app's views. catalog() shows every
open trail across all parks. trails_by_park() demonstrates a
cross-relation query (WP-705): given a park's id from the URL, it
filters trails using park__id, reaching across the ForeignKey from
Trail to Park. Both views reuse the same catalog.html template.

Functions:
    catalog(request)              : queries all open trails from the
                                     database, ordered by distance,
                                     and renders catalog.html
    trails_by_park(request, park_id) : queries open trails belonging
                                     to one specific park (cross-relation
                                     query via park__id), renders the
                                     same catalog.html template
"""

from django.shortcuts import render
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
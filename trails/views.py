"""
Application Programming CCGC 5003  Summer 2026
Humber College Institute of Technology and Advanced Learning
Waypoint - Web App
Part 6 - The Database (WP-605)
Developed by (IATIDEL AKIK N10038365)

Description:
This module defines the trails app's views - currently just the
public catalog, which queries the database for open trails and
renders them using the same catalog.html template from Week 11,
unmodified.

Functions:
    catalog(request) : queries open trails from the database,
                        ordered by distance, and renders catalog.html
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

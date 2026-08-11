"""
Application Programming CCGC 5003  Summer 2026
Humber College Institute of Technology and Advanced Learning
Waypoint - Web App
Part 3/4 - Pages and Forms (WP-402)
Developed by (IATIDEL AKIK N10038365)

Description:
This module defines the views for the Waypoint site - the Python
functions that handle incoming requests and decide what page (template)
to send back, and what data (context) that page should display.

Functions:
    home(request) : renders the homepage, greeting the visitor by name
"""

# render() builds an HttpResponse from a template + data
from django.shortcuts import render


def home(request):
    """
    Renders the homepage. Passes a context variable (site_name) that
    the template uses to greet the visitor.
    Parameters:
        request (HttpRequest): the incoming request object
    Returns:
        HttpResponse: the rendered home.html page
    """
    # This dict is the "context" - data made available inside the template
    context = {"site_name": "Waypoint"}
    # Combines home.html + context into a finished HTML page to send back
    return render(request, "home.html", context)
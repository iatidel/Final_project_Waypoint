"""
Application Programming CCGC 5003  Summer 2026
Humber College Institute of Technology and Advanced Learning
Waypoint - Web App
Part 3/4 - Pages and Forms (WP-402, WP-403, WP-404)
Developed by (IATIDEL AKIK N10038365)

Description:
This module defines the views for the Waypoint site - the Python
functions that handle incoming requests and decide what page (template)
to send back, and what data (context) that page should display.

Functions:
    home(request)   : renders the homepage, greeting the visitor by name
    report(request) : GET shows a blank trail-report form; POST reads
                       the submitted data and renders a personalized
                       thank-you page
    search(request) : safely reads the "q" query parameter and renders
                       the search results page, defaulting to "" if
                       no query was provided
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

def report(request):
    """
    Handles the trail report form. GET shows a blank form. POST reads
    the submitted data and renders a personalized thank-you page.
    Parameters:
        request (HttpRequest): the incoming request object
    Returns:
        HttpResponse: either the blank form (GET) or a thank-you page (POST)
    """
    if request.method == "POST":
        # Read each submitted field by its form input's "name" attribute.
        # .get() is used instead of [] so a missing field doesn't crash -
        # it just returns an empty string instead.
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        trail = request.POST.get("trail", "")
        note = request.POST.get("note", "")

        # Pass the submitted values into the thank-you page's context
        context = {"name": name, "email": email, "trail": trail, "note": note}
        return render(request, "thank_you.html", context)

    # GET request - just show the blank form
    return render(request, "report.html")

def search(request):
    """
    Handles trail search. Safely reads the "q" query parameter from
    the URL - if missing (e.g. someone visits /search/ with no query),
    defaults to an empty string instead of crashing.
    Parameters:
        request (HttpRequest): the incoming request object
    Returns:
        HttpResponse: the rendered search results page
    """
    # .get() with a default avoids a crash if "q" isn't in the URL at all
    query = request.GET.get("q", "")

    context = {"query": query}
    return render(request, "search.html", context)
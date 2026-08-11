"""
Application Programming CCGC 5003  Summer 2026
Humber College Institute of Technology and Advanced Learning
Waypoint - Web App
Part 3/4/5 - Pages, Forms, and Catalog (WP-405, WP-503)
Developed by (IATIDEL AKIK N10038365)

Description:
This module maps every URL in the site to the view function that
should handle it. Django checks each path() in order, top to bottom,
and calls the matching view.
"""

from django.contrib import admin
from django.urls import path
from waypoint import views  # our views.py, containing home(), report(), search()

urlpatterns = [

    # Django's built-in admin panel
    path('admin/', admin.site.urls), 

    # empty string = the site's root URL ("/")                  
    path('', views.home, name='home'), 

    # /report/ - GET shows form, POST handles submission                 
    path('report/', views.report, name='report'), 

    # /search/?q=... - reads q safely via .get()      
    path('search/', views.search, name='search'), 

    # /catalog/ - lists all trails in a table
    path('catalog/', views.catalog, name='catalog'),  
]
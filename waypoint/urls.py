"""
Application Programming CCGC 5003  Summer 2026
Humber College Institute of Technology and Advanced Learning
Waypoint - Web App
Part 3/4 - Pages and Forms (WP-405)
Developed by (IATIDEL AKIK N10038365)

Description:
This module maps every URL in the site to the view function that
should handle it. Django checks each path() in order, top to bottom,
and calls the matching view.
"""

from django.contrib import admin
from django.urls import path
# our views.py, containing home()
from waypoint import views 

urlpatterns = [
    # Django's built-in admin panel
    path('admin/', admin.site.urls),   
    # empty string = the site's root URL ("/")
    path('', views.home, name='home'),    
]
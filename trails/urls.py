"""
Application Programming CCGC 5003  Summer 2026
Humber College Institute of Technology and Advanced Learning
Waypoint - Web App
Part 6 - The Database (WP-605)
Developed by (IATIDEL AKIK N10038365)

Description:
This module maps URLs within the trails app to their views.
Mounted under /trails/ by the main project's urls.py via include().
"""

from django.urls import path
from . import views

urlpatterns = [
    # /trails/ - lists open trails from the database
    path('', views.catalog, name='trail_catalog'), 

    # /trails/park/<id>/ - cross-relation query, only that park's open trails
    path('park/<int:park_id>/', views.trails_by_park, name='trails_by_park'),
]
"""
Application Programming CCGC 5003  Summer 2026
Humber College Institute of Technology and Advanced Learning
Waypoint - Web App
Part 6/7/8 - Database, Relationships, and Hardening (WP-605, WP-705, WP-801)
Developed by (IATIDEL AKIK N10038365)

Description:
This module maps URLs within the trails app to their views.
Mounted under /trails/ by the main project's urls.py via include().

Note on ordering: park/<int:park_id>/ is listed before <int:trail_id>/
so Django's URL matcher checks the more specific "park/..." pattern
first - otherwise a URL like /trails/park/1/ could be misinterpreted
as trying to match trail_id="park" (which would fail anyway since
park_id/trail_id are typed as int, but keeping specific patterns
above general ones is good practice regardless).
"""

from django.urls import path
from . import views

urlpatterns = [
    # /trails/ - lists open trails from the database
    path('', views.catalog, name='trail_catalog'), 

    # /trails/park/<id>/ - cross-relation query, only that park's open trails
    path('park/<int:park_id>/', views.trails_by_park, name='trails_by_park'),

    # /trails/<id>/ - one trail's details, 404 if not found
    path('<int:trail_id>/', views.trail_detail, name='trail_detail'), 
]
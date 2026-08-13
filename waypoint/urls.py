"""
Application Programming CCGC 5003  Summer 2026
Humber College Institute of Technology and Advanced Learning
Waypoint - Web App
Part 3/4/5/6 - Pages, Forms, Catalog, and Database (WP-405, WP-503, WP-605)
Developed by (IATIDEL AKIK N10038365)

Description:
This module maps every URL in the site to the view function that
should handle it. Django checks each path() in order, top to bottom,
and calls the matching view. URLs starting with /trails/ are handed
off to the trails app's own urls.py via include().
"""

from django.contrib import admin
from django.urls import path, include
# our views.py, containing home(), report(), search(), catalog()
from waypoint import views

urlpatterns = [

    # Django's built-in admin panel
    path('admin/', admin.site.urls),

    # empty string = the site's root URL ("/")
    path('', views.home, name='home'),

    # /report/ - GET shows form, POST handles submission
    path('report/', views.report, name='report'),

    # /search/?q=... - reads q safely via .get()
    path('search/', views.search, name='search'),

    # /catalog/ - the OLD Week 11 catalog, still using hardcoded dicts
    path('catalog/', views.catalog, name='catalog'),

    # /trails/ - the NEW database-backed catalog (WP-605), hands off
    # everything under this prefix to trails/urls.py
    path('trails/', include('trails.urls')),
]
"""
Application Programming CCGC 5003  Summer 2026
Humber College Institute of Technology and Advanced Learning
Waypoint - Web App
Part 6/7 - The Database and Relationships (WP-604, WP-704)
Developed by (IATIDEL AKIK N10038365)

Description:
This module registers the Trail and Park models with Django's admin
panel, customizing how each appears - which columns show in the
list view, and which fields are searchable. TrailAdmin's list_display
now includes "park", so an admin can see each trail's assigned park
at a glance, and assign/change it directly from the trail list or
edit form.

Classes:
    TrailAdmin(admin.ModelAdmin) : customizes Trail's admin display
    ParkAdmin(admin.ModelAdmin)  : customizes Park's admin display
"""

from django.contrib import admin
from .models import Trail, Park


class TrailAdmin(admin.ModelAdmin):
    """
    Customizes how Trail appears in the Django admin panel.
    """
    # Columns shown in the admin's trail list view - "park" added
    # so an admin can see (and later filter/search by) each trail's
    # assigned park directly from the list
    list_display = ("name", "distance_km", "elevation_gain", "difficulty", "is_open", "park")

    # Fields the admin search box will search through
    search_fields = ("name",)


class ParkAdmin(admin.ModelAdmin):
    """
    Customizes how Park appears in the Django admin panel.
    """
    # Columns shown in the admin's park list view
    list_display = ("name", "region")

    # Fields the admin search box will search through
    search_fields = ("name",)

admin.site.register(Trail, TrailAdmin)
admin.site.register(Park, ParkAdmin)
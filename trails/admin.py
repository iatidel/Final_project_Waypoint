"""
Application Programming CCGC 5003  Summer 2026
Humber College Institute of Technology and Advanced Learning
Waypoint - Web App
Part 6 - The Database (WP-604)
Developed by (IATIDEL AKIK N10038365)

Description:
This module registers the Trail model with Django's admin panel,
customizing how it appears - which columns show in the list view,
and which fields are searchable.

Classes:
    TrailAdmin(admin.ModelAdmin) : customizes Trail's admin display
"""

from django.contrib import admin
from .models import Trail


class TrailAdmin(admin.ModelAdmin):
    """
    Customizes how Trail appears in the Django admin panel.
    """
    # Columns shown in the admin's trail list view
    list_display = ("name", "distance_km", "elevation_gain", "difficulty", "is_open")

    # Fields the admin search box will search through
    search_fields = ("name",)


admin.site.register(Trail, TrailAdmin)
"""
Application Programming CCGC 5003  Summer 2026
Humber College Institute of Technology and Advanced Learning
Waypoint - Web App
Part 6 - The Database (WP-602)
Developed by (IATIDEL AKIK N10038365)

Description:
This module defines the Trail model - the database version of the
Trail concept from Week 7's waypoint_core. Unlike the plain-Python
Trail class, this Trail is a Django model: each instance is saved
as a row in the database (via the ORM), and each field below becomes
a column in that row's table.

Classes:
    Trail(models.Model) : a hiking trail, stored in the database
"""

from django.db import models


class Trail(models.Model):
    """
    Represents a hiking trail stored in the database. Mirrors the
    fields from waypoint_core.Trail (Week 7), but as Django model
    fields instead of plain Python attributes - Django handles
    saving, loading, and validating this data against the database.
    """

    # Trail name - plain text, capped at 200 characters
    name = models.CharField(max_length=200)

    # Distance in km - DecimalField instead of float, to avoid
    # binary floating-point rounding errors; up to 6 total digits,
    # 2 of them after the decimal point (max value: 9999.99)
    distance_km = models.DecimalField(max_digits=6, decimal_places=2)

    # Elevation gain in meters - a whole number, no decimals needed
    elevation_gain = models.IntegerField()

    # Difficulty rating - restricted to exactly these 4 choices.
    # Each tuple is (value stored in the database, label shown to humans)
    difficulty = models.CharField(max_length=20, choices=[
        ("easy", "Easy"),
        ("moderate", "Moderate"),
        ("hard", "Hard"),
        ("expert", "Expert"),
    ])

    # Whether the trail is currently open - defaults to True (open)
    # if not explicitly set when creating a Trail
    is_open = models.BooleanField(default=True)

    # Automatically records the exact moment this row was first
    # created - Django fills this in on its own, never set manually
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns a human-readable representation of this Trail -
        used by the Django admin panel to display each row by name
        instead of a generic "Trail object (1)".
        Parameters: None
        Returns:
            str: the trail's name
        """
        return self.name
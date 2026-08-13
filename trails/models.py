"""
Application Programming CCGC 5003  Summer 2026
Humber College Institute of Technology and Advanced Learning
Waypoint - Web App
Part 6/7 - The Database and Relationships (WP-602, WP-701, WP-702)
Developed by (IATIDEL AKIK N10038365)

Description:
This module defines the Trail and Park models. Trail is the database
version of the Trail concept from Week 7's waypoint_core - each
instance is saved as a row in the database (via the ORM), and each
field becomes a column in that row's table. Park represents the
park a trail belongs to, added in Week 13 to model a real
one-to-many relationship (one park has many trails).

Trail links to Park via a ForeignKey using on_delete=SET_NULL: if a
park is deleted, its trails are NOT deleted along with it - they
simply become unassigned (park=NULL), since a trail's data remains
valuable even without a park. null=True/blank=True allow a trail to
exist with no park, both in the database and in admin forms - this
also covers trails created in Week 12, before this field existed.

Classes:
    Park(models.Model)  : a park that trails belong to
    Trail(models.Model) : a hiking trail, stored in the database,
                           optionally linked to one Park
"""

from django.db import models


class Park(models.Model):
    """
    Represents a park that trails belong to. Standalone model for
    now - the relationship to Trail is added in WP-702.
    """

    # Park name - plain text, capped at 200 characters
    name = models.CharField(max_length=200)

    # Region the park is located in (e.g. a province, state, or area)
    region = models.CharField(max_length=100)

    def __str__(self):
        """
        Returns a human-readable representation of this Park -
        used by the Django admin panel to display each row by name
        instead of a generic "Park object (1)".
        Parameters: None
        Returns:
            str: the park's name
        """
        return self.name


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

    # Links this trail to a Park. SET_NULL (not CASCADE) because
    # deleting a park shouldn't destroy its trails - the trail data
    # is still valuable even if unassigned. null=True/blank=True let
    # a trail exist with no park (required for SET_NULL, and covers
    # existing trails created before this field existed).
    park = models.ForeignKey(
        Park,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

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
"""
Application Programming CCGC 5003  Summer 2026
Humber College Institute of Technology and Advanced Learning
Waypoint - Domain Engine
Part 2 - Many Trail Types (WP-203)
Developed by (IATIDEL AKIK N10038365)

Description:
This module defines GuidedDayHike, a second level of inheritance:
a DayHike led by a professional guide. Adds one new field
(guide_name) on top of everything DayHike already provides.
Demonstrates a 3-level hierarchy: Trail -> DayHike -> GuidedDayHike.

Classes:
    GuidedDayHike(id, name, distance, elevation_gain_m, difficulty, guide_name)

Class methods:
    summary() : overridden to also mention the guide's name
    (estimated_time() and everything else is inherited unchanged from DayHike)
"""

from waypoint_core.day_hike import DayHike


class GuidedDayHike(DayHike):
    """
    A day hike led by a professional guide. Extends DayHike with one
    additional field: guide_name. Third level in the hierarchy
    (Trail -> DayHike -> GuidedDayHike).
    """

    def __init__(self, id, name, distance, elevation_gain_m, difficulty, guide_name):
        """
        Constructor: creates a GuidedDayHike. Delegates the DayHike
        fields to DayHike's constructor via super(), then adds the
        new guide_name field.
        Parameters:
            id (int): the unique identifier for the trail
            name (str): the name of the trail
            distance (Distance): the distance of the trail
            elevation_gain_m (float): the elevation gain in meters
            difficulty (str): the difficulty rating
            guide_name (str): the name of the guide leading this hike
        Returns:
            None
        """
        # super() here calls DayHike.__init__, which in turn calls
        # Trail.__init__ - each level only sets up its own piece
        super().__init__(id, name, distance, elevation_gain_m, difficulty)
        self.guide_name = guide_name

    def summary(self):
        """
        One-line description, overriding DayHike's summary() to also
        mention the guide leading the hike.
        Parameters: None
        Returns:
            str: summary text including the guide's name
        """
        return f"Guided Day Hike: {self.name} ({self.distance.magnitude}{self.distance.unit}, {self.difficulty}) led by {self.guide_name}"
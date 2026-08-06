"""
Application Programming CCGC 5003  Summer 2026
Humber College Institute of Technology and Advanced Learning
Waypoint - Domain Engine
Part 2 - Many Trail Types (WP-201, WP-203)
Developed by (IATIDEL AKIK N10038365)

Description:
This module defines TrailRun, a concrete Trail subclass representing
a trail running route. Pacing model (our own design): runs at
9 km/h - much faster than walking - plus 1 extra hour for every 900m
of elevation gain, a lighter penalty than the hiking types since a
runner (no heavy pack) handles climbs relatively more efficiently.

TrailRun does not add any new fields of its own - its __init__
simply delegates to Trail's constructor via super().

Classes:
    TrailRun(id, name, distance, elevation_gain_m, difficulty)

Class methods:
    estimated_time() : hours to complete, based on distance + elevation
    summary()         : one-line description of the run
"""

from waypoint_core.trail import Trail

# Pacing constants for TrailRun (see module docstring for reasoning)
RUN_PACE_KMH = 9.0            # km per hour, running pace
ELEVATION_PENALTY_M = 900     # meters of gain that add 1 extra hour


class TrailRun(Trail):
    """
    A trail running route. Concrete Trail subclass implementing
    estimated_time() and summary().
    """
    def __init__(self, id, name, distance, elevation_gain_m, difficulty):
            """
              Constructor: creates a TrailRun. Delegates all setup to Trail's
              constructor via super() - TrailRun doesn't add any new fields.
              Parameters:
                  id (int): the unique identifier for the trail
                  name (str): the name of the trail
                  distance (Distance): the distance of the trail
                  elevation_gain_m (float): the elevation gain in meters
                  difficulty (str): the difficulty rating
              Returns:
                 None
            """
            super().__init__(id, name, distance, elevation_gain_m, difficulty)
    

    def estimated_time(self):
        """
        Estimated hours to complete this run: distance (in km) at
        RUN_PACE_KMH, plus 1 hour per ELEVATION_PENALTY_M of gain.
        Parameters: None
        Returns:
            float: estimated hours
        """
        # Convert distance to km first, since our pacing constant is in km
        distance_km = self.distance.convert("km").magnitude

        # Time to cover the flat distance at running pace
        flat_time = distance_km / RUN_PACE_KMH

        # Extra time for climbing - lighter penalty than hiking types,
        # since a runner isn't carrying a heavy pack
        elevation_time = self.elevation_gain_m / ELEVATION_PENALTY_M

        # Total estimated time
        return flat_time + elevation_time

    def summary(self):
        """
        One-line human-readable description of this trail run.
        Parameters: None
        Returns:
            str: summary text
        """
        return f"Trail Run: {self.name} ({self.distance.magnitude}{self.distance.unit}, {self.difficulty})"
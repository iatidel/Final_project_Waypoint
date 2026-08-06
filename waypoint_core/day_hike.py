"""
Application Programming CCGC 5003  Summer 2026
Humber College Institute of Technology and Advanced Learning
Waypoint - Domain Engine
Part 2 - Many Trail Types (WP-201, WP-203)
Developed by (IATIDEL AKIK N10038365)

Description:
This module defines DayHike, a concrete Trail subclass representing
a single-day hike. Pacing model (loosely inspired by Naismith's Rule,
adapted with our own constants): walks at 4 km/h on flat ground, plus
1 extra hour for every 600m of elevation gain, to account for
climbing being slower than flat walking.

DayHike does not add any new fields of its own - its __init__ simply
delegates to Trail's constructor via super().

Classes:
    DayHike(id, name, distance, elevation_gain_m, difficulty)

Class methods:
    estimated_time() : hours to complete, based on distance + elevation
    summary()         : one-line description of the hike
"""

from waypoint_core.trail import Trail

# Pacing constants for DayHike (see module docstring for reasoning)
FLAT_PACE_KMH = 4.0          # km per hour on flat ground
ELEVATION_PENALTY_M = 600    # meters of gain that add 1 extra hour


class DayHike(Trail):
    """
    A single-day hike. Concrete Trail subclass implementing
    estimated_time() and summary().
    """
    def __init__(self, id, name, distance, elevation_gain_m, difficulty):
        """
          Constructor: creates a DayHike. Delegates all setup to Trail's
          constructor via super() - DayHike doesn't add any new fields.
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
        Estimated hours to complete this day hike: distance (in km)
        at FLAT_PACE_KMH, plus 1 hour per ELEVATION_PENALTY_M of gain.
        Parameters: None
        Returns:
            float: estimated hours
        """
        # Convert distance to km first, regardless of stored unit
        distance_km = self.distance.convert("km").magnitude
        # Time to cover the flat distance at our chosen flat pace
        flat_time = distance_km / FLAT_PACE_KMH
        # Extra time added for climbing - every ELEVATION_PENALTY_M meters
        # of elevation gain adds roughly 1 hour, since climbing is slower
        # than walking on flat ground
        elevation_time = self.elevation_gain_m / ELEVATION_PENALTY_M
        # Total estimated time is just the two parts added together
        return flat_time + elevation_time

    def summary(self):
        """
        One-line human-readable description of this day hike.
        Parameters: None
        Returns:
            str: summary text
        """
        return f"Day Hike: {self.name} ({self.distance.magnitude}{self.distance.unit}, {self.difficulty})"
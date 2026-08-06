"""
Application Programming CCGC 5003  Summer 2026
Humber College Institute of Technology and Advanced Learning
Waypoint - Domain Engine
Part 2 - Many Trail Types (WP-201, WP-203, WP-204)
Developed by (IATIDEL AKIK N10038365)

Description:
This module defines BackpackingRoute, a concrete Trail subclass
representing a multi-day backpacking trip. Pacing model (our own
design, adapted from DayHike's approach): walks at 2.5 km/h - slower
than a day hike since carrying a full pack - plus 1 extra hour for
every 400m of elevation gain, a steeper penalty than DayHike since
climbing with a loaded pack is more strenuous.

BackpackingRoute does not add any new fields of its own - its
__init__ simply delegates to Trail's constructor via super().

BackpackingRoute also overrides packing_list() to EXTEND Trail's
baseline gear list (via super()) with backpacking-specific items,
rather than replacing it from scratch (WP-204).

Classes:
    BackpackingRoute(id, name, distance, elevation_gain_m, difficulty)

Class methods:
    estimated_time() : hours to complete, based on distance + elevation
    summary()         : one-line description of the route
    packing_list()    : overridden - baseline gear PLUS backpacking gear
"""

from waypoint_core.trail import Trail

# Pacing constants for BackpackingRoute (see module docstring for reasoning)
PACK_PACE_KMH = 2.5           # km per hour, slower due to full pack
ELEVATION_PENALTY_M = 400     # meters of gain that add 1 extra hour


class BackpackingRoute(Trail):
    """
    A multi-day backpacking route. Concrete Trail subclass implementing
    estimated_time() and summary().
    """
    def __init__(self, id, name, distance, elevation_gain_m, difficulty):
            """
              Constructor: creates a BackpackingRoute. Delegates all setup to Trail's
              constructor via super() - BackpackingRoute doesn't add any new fields.
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
        Estimated hours to complete this route: distance (in km) at
        PACK_PACE_KMH, plus 1 hour per ELEVATION_PENALTY_M of gain.
        Parameters: None
        Returns:
            float: estimated hours
        """
        # Convert distance to km first, since our pacing constant is in km
        distance_km = self.distance.convert("km").magnitude

        # Time to cover the flat distance at backpacking pace
        flat_time = distance_km / PACK_PACE_KMH

        # Extra time for climbing with a loaded pack - steeper penalty
        # than DayHike since weight makes climbing harder
        elevation_time = self.elevation_gain_m / ELEVATION_PENALTY_M

        # Total estimated time
        return flat_time + elevation_time

    def summary(self):
        """
        One-line human-readable description of this backpacking route.
        Parameters: None
        Returns:
            str: summary text
        """
        return f"Backpacking Route: {self.name} ({self.distance.magnitude}{self.distance.unit}, {self.difficulty})"

    def packing_list(self):
        """
        Extends Trail's baseline packing list with gear specific to
        multi-day backpacking trips.
        Parameters: None
        Returns:
            list[str]: baseline gear PLUS backpacking-specific gear
        """
        # Get the baseline list from Trail first, instead of rewriting it
        base_items = super().packing_list()
        # Add backpacking-specific gear on top
        return base_items + ["tent", "sleeping bag", "camp stove"]
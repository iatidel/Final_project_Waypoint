"""
Application Programming CCGC 5003  Summer 2026
Humber College Institute of Technology and Advanced Learning
Waypoint - Domain Engine
Part 2 - Many Trail Types (WP-205)
Developed by (IATIDEL AKIK N10038365)

Description:
This module defines RatedBackpackingRoute, a BackpackingRoute composed
with both ElevationMixin and RatingMixin via multiple inheritance.
Demonstrates MRO (Method Resolution Order): Python searches
RatedBackpackingRoute -> BackpackingRoute -> ElevationMixin ->
RatingMixin -> Trail -> ABC -> object, in that left-to-right order,
when looking up any method not defined directly on this class.

Classes:
    RatedBackpackingRoute(id, name, distance, elevation_gain_m, difficulty)
"""

from waypoint_core.backpacking_route import BackpackingRoute
from waypoint_core.mixins import ElevationMixin, RatingMixin


class RatedBackpackingRoute(BackpackingRoute, ElevationMixin, RatingMixin):
    """
    A BackpackingRoute that also supports grade_percent() (from
    ElevationMixin) and average_rating()/add_rating() (from RatingMixin).
    """

    def __init__(self, id, name, distance, elevation_gain_m, difficulty):
        """
        Constructor: initializes the full chain via super(), which
        follows the MRO - BackpackingRoute's __init__ runs first,
        then (because RatingMixin also calls super().__init__())
        RatingMixin's __init__ runs too, setting up self._ratings.
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
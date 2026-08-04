"""
Application Programming CCGC 5003  Summer 2026
Humber College Institute of Technology and Advanced Learning
Waypoint - Domain Engine
Part 1 - The Trail Model (WP-105)
Developed by (IATIDEL AKIK N10038365)

Description:
This module defines the Itinerary class, representing an ordered
trip made up of multiple Trail objects, and computing the total
distance across all of them (handling unit conversion safely).

Classes:
    Itinerary(unit="km") : represents an ordered list of trails

Class methods:
    trails (property)         : read-only access to the ordered list of trails
    add_trail(trail)          : appends a trail to the itinerary
    total_distance()          : returns a Distance, the sum of all trail distances
"""

from waypoint_core.distance import Distance


class Itinerary:
    """
    Represents a trip: an ordered list of trails, with the ability
    to compute the combined total distance across all of them.
    """

    def __init__(self, unit="km"):
        """
        Constructor: creates an empty Itinerary.
        Parameters:
            unit (str): the unit used when reporting total_distance(),
                        defaults to "km"
        Returns:
            None
        """
        self._trails = []       # ordered list of Trail objects
        self._unit = unit       # unit total_distance() will report in

    @property
    def trails(self):
        """
        Read-only access to the ordered list of trails.
        Parameters: None
        Returns:
            list[Trail]: the trails in this itinerary, in order
        """
        return self._trails

    def add_trail(self, trail):
        """
        Appends a trail to the end of the itinerary.
        Parameters:
            trail (Trail): the trail to add
        Returns:
            None
        """
        self._trails.append(trail)

    def total_distance(self):
        """
        Computes the combined distance of every trail in the itinerary,
        converting each to self._unit first so units are never mixed.
        Parameters: None
        Returns:
            Distance: the total distance, in self._unit
        """
        total = 0
        # Convert every trail's distance to a common unit before summing,
        # otherwise adding raw magnitudes could mix km and mi (WP-105)
        for trail in self._trails:
            converted = trail.distance.convert(self._unit)
            total += converted.magnitude
        return Distance(total, self._unit)
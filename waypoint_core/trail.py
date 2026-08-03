"""
Application Programming CCGC 5003  Summer 2026
Humber College Institute of Technology and Advanced Learning
Waypoint - Domain Engine
Part 1 - The Trail Model (WP-102, WP-103)
Developed by (IATIDEL AKIK N10038365)

Description:
This module defines the Trail class, representing a single hiking
trail with a name, a Distance, elevation gain, and a difficulty
rating that is validated on both creation and later changes.
It also provides an alternate constructor (from_dict) to build a
Trail from a dictionary (e.g. API-shaped data), and a static
validator for difficulty values.

Classes:
    Trail (name, distance, elevation_gain_m, difficulty) : represents a trail

Class variables:
    ALLOWED_DIFFICULTIES (list) : the only valid difficulty strings
    DEFAULT_UNIT (str)          : the platform-wide default distance unit

Class methods:
    distance (property)              : read-only access to the distance
    difficulty (property)            : read-only access to the difficulty
    set_difficulty(new_difficulty)   : validates and updates difficulty
    from_dict(data)                  : classmethod, builds a Trail from a dict
    is_valid_difficulty(difficulty)  : staticmethod, checks a difficulty string
"""

from waypoint_core.distance import Distance

class Trail:
    """
    Represents a hiking trail with a name, distance, elevation gain, 
    and difficulty rating.
    """

    # Class variable : the only allowed difficulty value 
    ALLOWED_DIFFICULTIES = ["easy", "moderate", "hard", "expert"]

    # Class variable: the platform's default distance unit for new trails
    # built through from_dict() when no unit is otherwise specified
    DEFAULT_UNIT = "km"

    def __init__(self, name, distance, elevation_gain_m, difficulty):
        """
        Constructor: creates a Trail object.
        Parameters:
            name (str): the name of the trail
            distance (Distance): the distance of the trail
            elevation_gain_m (float): the elevation gain in meters
            difficulty (str): the difficulty rating, must be one of ALLOWED_DIFFICULTIES
        Returns:
            None
        """
        self.name = name
        self._distance = distance
        self.elevation_gain_m = elevation_gain_m
        self._difficulty = None  # placeholder, real value set by set_difficulty below
        self.set_difficulty(difficulty)  # validate and set difficulty


    def set_difficulty(self, difficulty):
        """
        Validates and sets the difficulty rating for the trail.
        Reuses is_valid_difficulty() so the validation rule lives in one place.
        Parameters:
            difficulty (str): the new difficulty rating
        Returns:
            None
        """
        if not Trail.is_valid_difficulty(difficulty):
            raise ValueError(f"Invalid difficulty. Must be one of {self.ALLOWED_DIFFICULTIES}")
        self._difficulty = difficulty

    @property
    def difficulty(self):
        """
        Read-only property to access the difficulty rating of the trail.
        Parameters:
            None
        Returns:
            str: the difficulty rating
        """
        return self._difficulty

    @property
    def distance(self):
        """
        Read-only property to access the distance of the trail.
        Parameters:
            None
        Returns:
            Distance: the distance object representing the trail's length
        """
        return self._distance

    @classmethod
    def from_dict(cls, data):
        """
        Alternate constructor: builds a Trail from an API-shaped dict.
        Uses DEFAULT_UNIT if no unit is provided in the data.
        Parameters:
            data (dict): expected keys -
                        "name" (str), "distance_magnitude" (float),
                        "distance_unit" (str, optional), "elevation_gain_m" (float),
                        "difficulty" (str)
        Returns:
            Trail: a new Trail object built from the dict
        """
        unit = data.get("distance_unit", cls.DEFAULT_UNIT)
        distance = Distance(data["distance_magnitude"], unit)
        return cls(data["name"], distance, data["elevation_gain_m"], data["difficulty"])

    @staticmethod
    def is_valid_difficulty(difficulty):
        """
        Checks whether a difficulty string is one of the allowed values.
        Parameters:
            difficulty (str): the difficulty to check
        Returns:
            bool: True if valid, False otherwise
        """
        return difficulty in Trail.ALLOWED_DIFFICULTIES



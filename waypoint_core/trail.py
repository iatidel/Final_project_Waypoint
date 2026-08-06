"""
Application Programming CCGC 5003  Summer 2026
Humber College Institute of Technology and Advanced Learning
Waypoint - Domain Engine
Part 1/2 - The Trail Model + Hierarchy (WP-102, WP-103, WP-104, WP-201)
Developed by (IATIDEL AKIK N10038365)

Description:
This module defines the Trail abstract base class, representing the
shared shape of every hiking trail: an id, name, Distance, elevation
gain, and a validated difficulty rating. Trail cannot be instantiated
directly - concrete subclasses (DayHike, BackpackingRoute, TrailRun,
defined in other modules) must implement estimated_time() and
summary(). Trail also provides an alternate constructor (from_dict),
a static validator for difficulty values, and equality comparison by id.

Classes:
    Trail (id, name, distance, elevation_gain_m, difficulty) : abstract base class

Class variables:
    ALLOWED_DIFFICULTIES (list) : the only valid difficulty strings
    DEFAULT_UNIT (str)          : the platform-wide default distance unit

Class methods:
    distance (property)              : read-only access to the distance
    difficulty (property)            : read-only access to the difficulty
    set_difficulty(new_difficulty)   : validates and updates difficulty
    from_dict(data)                  : classmethod, builds a Trail from a dict
    is_valid_difficulty(difficulty)  : staticmethod, checks a difficulty string
    __eq__(other)                    : compares two Trails by id
    estimated_time()                 : ABSTRACT - subclasses must implement
    summary()                        : ABSTRACT - subclasses must implement
"""

# NEW: needed to make Trail an abstract base class
from abc import ABC, abstractmethod
from waypoint_core.distance import Distance


# CHANGED: Trail now inherits from ABC instead of nothing
class Trail(ABC):
    """
    Abstract base class representing a hiking trail. Cannot be
    instantiated directly - every concrete subclass must implement
    estimated_time() and summary().
    """

    # Class variable: the only allowed difficulty values
    ALLOWED_DIFFICULTIES = ["easy", "moderate", "hard", "expert"]

    # Class variable: the platform's default distance unit for new trails
    # built through from_dict() when no unit is otherwise specified
    DEFAULT_UNIT = "km"

    def __init__(self, id, name, distance, elevation_gain_m, difficulty):
        """
        Constructor: creates a Trail object. Only ever called via a
        subclass, since Trail itself is abstract and cannot be
        instantiated directly.
        Parameters:
            id (int): the unique identifier for the trail
            name (str): the name of the trail
            distance (Distance): the distance of the trail
            elevation_gain_m (float): the elevation gain in meters
            difficulty (str): the difficulty rating, must be one of ALLOWED_DIFFICULTIES
        Returns:
            None
        """
        self.id = id
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
        Parameters: None
        Returns:
            str: the difficulty rating
        """
        return self._difficulty

    @property
    def distance(self):
        """
        Read-only property to access the distance of the trail.
        Parameters: None
        Returns:
            Distance: the distance object representing the trail's length
        """
        return self._distance

    @classmethod
    def from_dict(cls, data):
        """
        Alternate constructor: builds a Trail (subclass) from an
        API-shaped dict. Uses DEFAULT_UNIT if no unit is provided.
        Parameters:
            data (dict): expected keys -
                "id" (int), "name" (str), "distance_magnitude" (float),
                "distance_unit" (str, optional), "elevation_gain_m" (float),
                "difficulty" (str)
        Returns:
            Trail: a new Trail subclass object built from the dict
        """
        unit = data.get("distance_unit", cls.DEFAULT_UNIT)
        distance = Distance(data["distance_magnitude"], unit)
        # NOTE: order here must match __init__'s parameter order exactly
        return cls(data["id"], data["name"], distance, data["elevation_gain_m"], data["difficulty"])

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

    def __eq__(self, other):
        """
        Checks equality between two Trail objects based on their id.
        Two trails with the same id are considered equal, even if other
        fields differ - used to de-duplicate trails from imports.
        Parameters:
            other (object): the object to compare against
        Returns:
            bool: True if other is a Trail with the same id, False otherwise
        """
        # Guard: only compare against other Trail objects
        if not isinstance(other, Trail):
            return False
        return self.id == other.id

    # NEW: abstract methods below - every concrete subclass MUST implement
    # both, or Python will refuse to let that subclass be instantiated.

    @abstractmethod
    def estimated_time(self):
        """
        Returns the estimated time to complete this trail, in hours.
        Each subclass paces this differently (WP-202, WP-203, WP-204).
        Parameters: None
        Returns:
            float: estimated hours to complete the trail
        """
        pass

    @abstractmethod
    def summary(self):
        """
        Returns a short human-readable description of this trail.
        Each subclass formats this differently.
        Parameters: None
        Returns:
            str: a one-line summary
        """
        pass
"""
Application Programming CCGC 5003  Summer 2026
Humber College Institute of Technology and Advanced Learning
Waypoint - Domain Engine
Part 2 - Many Trail Types (WP-205)
Developed by (IATIDEL AKIK N10038365)

Description:
This module defines two mixins - small classes meant to be combined
with a Trail subclass via multiple inheritance to add one specific
capability each. Neither mixin is meant to be used standalone, and
neither defines __init__, since both just compute values from data
the host class (a Trail subclass) already has.

Classes:
    ElevationMixin : adds grade_percent(), the trail's average steepness
    RatingMixin     : adds average_rating(), from a list of star ratings
"""


class ElevationMixin:
    """
    Mixin adding elevation-grade calculation. Expects the class it's
    mixed into to already have self.elevation_gain_m and self.distance
    (i.e. it's meant to be combined with a Trail subclass, not used alone).
    """

    def grade_percent(self):
        """
        Computes the trail's average grade (steepness) as a percentage:
        elevation gained per meter traveled, times 100.
        Parameters: None
        Returns:
            float: grade as a percentage (e.g. 5.0 means 5% average grade)
        """
        # Convert distance to meters so both values share the same unit
        distance_m = self.distance.convert("km").magnitude * 1000
        if distance_m == 0:
            return 0.0
        return (self.elevation_gain_m / distance_m) * 100


class RatingMixin:
    """
    Mixin adding a star-rating system. Stores its own list of ratings,
    since this is new data no Trail subclass already has - so unlike
    ElevationMixin, this one DOES need to initialize something.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes an empty ratings list. Passes along any other
        args/kwargs via super() so this plays nicely in a multi-parent
        chain (see MRO discussion in guided_day_hike / composed class).
        Parameters:
            *args, **kwargs: passed through to the next class in the MRO
        Returns:
            None
        """
        super().__init__(*args, **kwargs)
        self._ratings = []

    def add_rating(self, stars):
        """
        Adds a new star rating (1-5) to this trail.
        Parameters:
            stars (int): a rating from 1 to 5
        Returns:
            None
        """
        if stars < 1 or stars > 5:
            raise ValueError("Rating must be between 1 and 5")
        self._ratings.append(stars)

    def average_rating(self):
        """
        Computes the average of all ratings so far.
        Parameters: None
        Returns:
            float: average star rating, or 0.0 if no ratings yet
        """
        if not self._ratings:
            return 0.0
        return sum(self._ratings) / len(self._ratings)
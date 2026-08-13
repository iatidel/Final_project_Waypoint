"""
Application Programming CCGC 5003  Summer 2026
Humber College Institute of Technology and Advanced Learning
Waypoint - Domain Engine
Part 2 - Many Trail Types (WP-206)
Developed by (IATIDEL AKIK N10038365)

Description:
Manual test script proving polymorphism and duck typing. Builds a
mixed list of real Trail subclasses (DayHike, BackpackingRoute,
TrailRun) plus FakeTrail - a class that does NOT inherit from Trail
at all - and runs a single loop calling estimated_time() on every
item. Proves Python only requires the method to exist at call time,
not any particular inheritance relationship.
"""

from waypoint_core.day_hike import DayHike
from waypoint_core.backpacking_route import BackpackingRoute
from waypoint_core.trail_run import TrailRun
from waypoint_core.distance import Distance


class FakeTrail:
    """
    A duck-typed stand-in for a Trail, useful for testing. Does NOT
    inherit from Trail at all - proves the polymorphic loop works
    based on having estimated_time(), not on inheritance.
    """
    def estimated_time(self):
        """
        Returns a fixed dummy time, for testing purposes.
        Parameters: None
        Returns:
            float: a hardcoded estimated time
        """
        return 1.0


# A mixed list: real Trail subclasses AND a completely unrelated FakeTrail
trails = [
    DayHike(1, "Forest Loop", Distance(10, "km"), 300, "easy"),
    BackpackingRoute(2, "Summit Trail", Distance(20, "km"), 800, "hard"),
    TrailRun(3, "Ridge Sprint", Distance(15, "km"), 900, "hard"),
    FakeTrail(),  # not a Trail subclass at all - duck typing in action
]

# One loop, works for every item regardless of its actual class
for t in trails:
    print(f"{type(t).__name__}: {t.estimated_time():.2f} hours")
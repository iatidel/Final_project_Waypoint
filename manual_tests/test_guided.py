from waypoint_core.guided_day_hike import GuidedDayHike
from waypoint_core.day_hike import DayHike
from waypoint_core.distance import Distance

hike = GuidedDayHike(4, "Alpine Loop", Distance(8, "km"), 500, "moderate", "Sam Rivera")
print(hike.summary())
print(f"Estimated time: {hike.estimated_time():.2f} hours")
print(f"Is a DayHike? {isinstance(hike, DayHike)}")
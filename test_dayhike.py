from waypoint_core.day_hike import DayHike
from waypoint_core.distance import Distance

hike = DayHike(1, "Sunrise Ridge", Distance(10, "km"), 600, "moderate")
print(hike.summary())
print(f"Estimated time: {hike.estimated_time():.2f} hours")
print(hike.packing_list())
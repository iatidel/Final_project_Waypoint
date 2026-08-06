from waypoint_core.rated_backpacking_route import RatedBackpackingRoute
from waypoint_core.distance import Distance

r = RatedBackpackingRoute(5, "Summit Trail", Distance(10, "km"), 500, "hard")

# Prove the MRO - the exact order Python searches for methods
print(RatedBackpackingRoute.__mro__)

# Test methods from BOTH mixins
print(f"Grade: {r.grade_percent():.2f}%")
r.add_rating(5)
r.add_rating(3)
print(f"Average rating: {r.average_rating()}")

# Prove it's STILL a full Trail (inherited estimated_time, summary, packing_list)
print(r.summary())
print(f"Estimated time: {r.estimated_time():.2f} hours")
print(r.packing_list())
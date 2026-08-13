from waypoint_core.backpacking_route import BackpackingRoute
from waypoint_core.distance import Distance

route = BackpackingRoute(2, "Wilderness Traverse", Distance(20, "km"), 800, "hard")
print(route.summary())
print(f"Estimated time: {route.estimated_time():.2f} hours")

# Test the packing list method WP-204
print(route.packing_list())
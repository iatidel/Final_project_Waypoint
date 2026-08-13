from waypoint_core.trail_run import TrailRun
from waypoint_core.distance import Distance

run = TrailRun(3, "Ridge Sprint", Distance(15, "km"), 900, "hard")
print(run.summary())
print(f"Estimated time: {run.estimated_time():.2f} hours")
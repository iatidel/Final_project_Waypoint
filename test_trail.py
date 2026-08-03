from waypoint_core.trail import Trail
from waypoint_core.distance import Distance

d = Distance(5, "km")
t = Trail("Test Trail", d, 100, "moderate")
#print(t.name, t.distance.magnitude, t.difficulty)
"""
try:
    bad_trail = Trail("Bad Trail", d, 100, "impossible")
except ValueError as e:
    print(f"Error creating trail: {e}")
    """
data = {"name": "River Loop", "distance_magnitude": 8, "elevation_gain_m": 200, "difficulty": "hard"}
t2 = Trail.from_dict(data)
print(t2.name, t2.distance.magnitude, t2.distance.unit, t2.difficulty)
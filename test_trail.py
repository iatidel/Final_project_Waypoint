from waypoint_core.trail import Trail
from waypoint_core.distance import Distance
"""
d = Distance(5, "km")
t = Trail(1, "Test Trail", d, 100, "moderate")
print(t.name, t.distance.magnitude, t.difficulty)

try:
    bad_trail = Trail(2, "Bad Trail", d, 100, "impossible")
except ValueError as e:
    print(f"Error creating trail: {e}")

data = {"id": 3, "name": "River Loop", "distance_magnitude": 8, "elevation_gain_m": 200, "difficulty": "hard"}
t2 = Trail.from_dict(data)
print(t2.name, t2.distance.magnitude, t2.distance.unit, t2.difficulty)

# Equality tests
t3 = Trail(1, "Renamed Trail", d, 999, "easy")   # same id as t, different everything else
print(t == t3)   # expect True - same id
print(t == t2)   # expect False - different id
print(t == "not a trail")  # expect False - not even a Trail
"""
#Abstract class test WEEK 08
# Proof that Trail is now abstract and cannot be instantiated directly
try:
    t = Trail(99, "Should Fail", Distance(5, "km"), 100, "easy")
except TypeError as e:
    print(f"Correctly blocked: {e}")
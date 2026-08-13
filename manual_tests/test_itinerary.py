from waypoint_core.trail import Trail
from waypoint_core.distance import Distance
from waypoint_core.itinerary import Itinerary

# Step 1: create some distances - mixed units on purpose
d1 = Distance(5, "km")
d2 = Distance(3, "mi")

# Step 2: wrap each distance in a Trail
# Trail(id, name, distance, elevation_gain_m, difficulty)
t1 = Trail(1, "Forest Loop", d1, 100, "easy")
t2 = Trail(2, "Mountain Path", d2, 300, "moderate")

# Step 3: create an itinerary (defaults to reporting totals in "km")
trip = Itinerary()

# Step 4: add the trails to the itinerary
trip.add_trail(t1)
trip.add_trail(t2)

# Step 5: compute the total distance
total = trip.total_distance()
print(f"Total distance: {total.magnitude} {total.unit}")

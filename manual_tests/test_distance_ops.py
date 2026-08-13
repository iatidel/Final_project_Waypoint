from waypoint_core.distance import Distance

a = Distance(3, "km")
b = Distance(2, "km")
c = Distance(2, "mi")

print(a + b)                # expect: 5 km
print(a - b)                # expect: 1 km
print(a == Distance(3, "km"))  # expect: True
print(a == c)                # expect: False (mixed units, no crash)
print(b < a)                  # expect: True
print(a > b)                  # expect: True
print(repr(a))                 # expect: Distance(3, 'km')

# Sorting a list of same-unit distances (uses __lt__ under the hood)
distances = [Distance(5, "km"), Distance(1, "km"), Distance(3, "km")]
distances.sort()
print(distances)

# Mixed-unit add should raise
try:
    a + c
except ValueError as e:
    print(f"Correctly blocked: {e}")
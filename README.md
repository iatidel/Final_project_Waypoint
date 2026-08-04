# Waypoint

A trail-finder and trip-planner app. Built solo across 8 weeks: first a
pure-Python domain engine (Weeks 7-8), then a Django web app around it
(Weeks 9-14).

## Status
Week 7 complete (tagged `w7`) — domain engine finished (Distance, Trail, Itinerary).
Week 8 in progress — trail hierarchy, polymorphism, operator overloading.

## Project structure
- `waypoint_core/` — pure-Python domain classes (Distance, Trail, Itinerary)
- `test_trail.py` — manual test script for Trail/Distance
- `test_itinerary.py` — manual test script for Itinerary
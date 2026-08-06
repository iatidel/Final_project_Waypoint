# Waypoint

A trail-finder and trip-planner app. Built solo across 8 weeks: first a
pure-Python domain engine (Weeks 7-8), then a Django web app around it
(Weeks 9-14).

## Status
Week 7 complete (tagged `w7`) — domain engine finished (Distance, Trail, Itinerary).
Week 8 complete (tagged `v8`) — trail hierarchy (DayHike, BackpackingRoute, TrailRun,
GuidedDayHike), Distance operator overloading, mixins (ElevationMixin, RatingMixin),
polymorphism and duck typing.
Week 9 starting — standing up the Django project.

## Project structure
- `waypoint_core/` — pure-Python domain classes
  - `distance.py` — Distance (validated, immutable, operator-overloaded)
  - `trail.py` — Trail (abstract base class)
  - `day_hike.py`, `backpacking_route.py`, `trail_run.py` — concrete Trail subclasses
  - `guided_day_hike.py` — extends DayHike (3rd inheritance level)
  - `mixins.py` — ElevationMixin, RatingMixin
  - `rated_backpacking_route.py` — composed class using both mixins
  - `itinerary.py` — Itinerary (ordered trail list, total distance)
- `test_*.py` — manual test scripts, one per feature/ticket
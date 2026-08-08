# Waypoint

A trail-finder and trip-planner app. Built solo across 8 weeks: first a
pure-Python domain engine (Weeks 7-8), then a Django web app around it
(Weeks 9-14).

## Status
Week 7 complete (tagged `w7`) — domain engine finished (Distance, Trail, Itinerary).
Week 8 complete (tagged `v8`) — trail hierarchy, operator overloading, mixins, polymorphism.
Week 9 complete (tagged `v9`) — Django project set up (venv, Django 4.2, dev server verified).
Week 10 starting — homepage and trail report form.

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

## Running the project

1. Clone the repo and `cd` into it.
2. Create and activate a virtual environment:
  python -m venv env
      Windows: `env\Scripts\Activate.ps1`
      Mac/Linux: `source env/bin/activate`
3. Install dependencies:
  pip install -r requirements.txt
4. Apply database migrations:
  python manage.py migrate
5. Run the development server:
  python manage.py runserver
6. Open `http://127.0.0.1:8000/` in your browser.


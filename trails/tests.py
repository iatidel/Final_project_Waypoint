"""
Application Programming CCGC 5003  Summer 2026
Humber College Institute of Technology and Advanced Learning
Waypoint - Web App
Part 8 - Hardening and Handoff (WP-801)
Developed by (IATIDEL AKIK N10038365)

Description:
This module contains automated tests for Waypoint. Unlike manual
testing (running the server and clicking around), these tests run
instantly and repeatably via `python manage.py test`.

TrailQueryTests and TrailDetailTests use django.test.TestCase, which
provides a temporary throwaway test database - nothing here ever
touches the real db.sqlite3. DistanceDomainRuleTests uses plain
unittest.TestCase instead, since it tests waypoint_core.Distance -
pure Python domain logic with no Django or database involvement.

Classes:
    TrailQueryTests(TestCase)          : tests for querying Trail data
    TrailDetailTests(TestCase)         : tests for the trail detail
                                          view's 404 behavior
    DistanceDomainRuleTests(unittest.TestCase) : unit tests for
                                          waypoint_core.Distance
"""

import unittest
from django.test import TestCase
from .models import Trail
from waypoint_core.distance import Distance


class TrailQueryTests(TestCase):
    """
    Tests for querying Trail data, specifically that closed trails
    are correctly excluded from the public catalog's query.
    """

    def test_only_open_trails_returned(self):
        """
        Creates one open and one closed trail, then confirms that
        filtering by is_open=True returns only the open one - the
        same query used in trails/views.py's catalog().
        Parameters: None (self only - test methods take no arguments)
        Returns: None
        """
        # Create two trails directly in the test database
        Trail.objects.create(
            name="Open Trail", distance_km=5.0, elevation_gain=100,
            difficulty="easy", is_open=True
        )
        Trail.objects.create(
            name="Closed Trail", distance_km=3.0, elevation_gain=50,
            difficulty="easy", is_open=False
        )

        # Run the same kind of query catalog() uses
        open_trails = Trail.objects.filter(is_open=True)

        # Assert: exactly one trail should come back, and it should
        # be the open one, not the closed one
        self.assertEqual(open_trails.count(), 1)
        self.assertEqual(open_trails.first().name, "Open Trail")


class TrailDetailTests(TestCase):
    """
    Tests for the trail detail view, specifically that requesting a
    non-existent trail id returns a proper 404 response.
    """

    def test_detail_404_for_missing_trail(self):
        """
        Requests a trail id that doesn't exist in the database, and
        confirms the response is a 404 - proving get_object_or_404
        is working correctly in trail_detail().
        Parameters: None
        Returns: None
        """
        # No trail with id 9999 has been created in this test's
        # database, so this request should fail with a 404
        response = self.client.get("/trails/9999/")
        self.assertEqual(response.status_code, 404)


class DistanceDomainRuleTests(unittest.TestCase):
    """
    Unit tests for waypoint_core.Distance - pure Python domain logic,
    no Django/database involved, so plain unittest.TestCase is used
    instead of django.test.TestCase.
    """

    def test_negative_magnitude_rejected(self):
        """
        Confirms Distance raises ValueError when given a negative
        magnitude, per the validation rule from Week 7.
        Parameters: None
        Returns: None
        """
        # assertRaises checks that the given exception is raised
        # inside the "with" block - the test fails if it ISN'T raised
        with self.assertRaises(ValueError):
            Distance(-5, "km")

    def test_add_same_unit_distances(self):
        """
        Confirms Distance.__add__ correctly sums two same-unit
        Distances, per the operator overloading from Week 8 (WP-202).
        Parameters: None
        Returns: None
        """
        result = Distance(3, "km") + Distance(2, "km")
        self.assertEqual(result.magnitude, 5)
        self.assertEqual(result.unit, "km")
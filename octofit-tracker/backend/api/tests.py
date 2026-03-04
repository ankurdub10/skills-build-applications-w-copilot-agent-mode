from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class RouterSmokeTests(APITestCase):
    """Simple smoke tests that each registered viewset has a working list URL.

    These don't exercise model behavior, just ensure the routes exist so that
    further development can rely on them being registered correctly.
    """

    def test_list_endpoints_exist(self):
        # mapping of url name prefixes to expected status codes
        endpoints = [
            'activity-list',
            'user-list',
            'team-list',
            'workout-list',
            'leaderboard-list',
        ]

        for name in endpoints:
            url = reverse(name)
            response = self.client.get(url)
            self.assertIn(response.status_code, (status.HTTP_200_OK, status.HTTP_204_NO_CONTENT))

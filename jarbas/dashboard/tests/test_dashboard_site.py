from unittest.mock import MagicMock, patch

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase

from jarbas.dashboard.sites import DashboardSite, DummyUser, dashboard

User = get_user_model()


class TestDashboardSite(TestCase):

    def setUp(self):
        self.site = dashboard

    def test_init(self):
        self.assertEqual({}, dict(self.site.actions))
        self.assertEqual({}, dict(self.site._global_actions))
        self.assertEqual('dashboard', self.site.name)

    def test_valid_url(self):
        valid, invalid = MagicMock(), MagicMock()
        valid.regex.pattern = '/whatever/'
        invalid.regex.pattern = '/whatever/add/'
        self.assertTrue(self.site.valid_url(valid))
        self.assertFalse(self.site.valid_url(invalid))

    @patch.object(DashboardSite, 'get_urls')
    @patch.object(DashboardSite, 'valid_url')
    def test_urls(self, valid_url, get_urls):
        valid_url.side_effect = (True, False, True)
        get_urls.return_value = range(3)
        expected = [0, 2], 'admin', 'dashboard'
        self.assertEqual(expected, self.site.urls)

    def test_has_permission_get(self):
        request = MagicMock()
        request.method = 'GET'
        self.assertTrue(self.site.has_permission(request))

    def test_has_permission_post(self):
        request = MagicMock()
        request.method = 'POST'
        self.assertFalse(self.site.has_permission(request))

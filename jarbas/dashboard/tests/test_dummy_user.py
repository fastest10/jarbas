from django.test import TestCase

from jarbas.dashboard.sites import DummyUser


class TestDummyUser(TestCase):

    def setUp(self):
        self.user = DummyUser()

    def test_has_module_perms(self):
        self.assertTrue(self.user.has_module_perms('core'))
        self.assertFalse(self.user.has_module_perms('api'))
        self.assertFalse(self.user.has_module_perms('dashboard'))
        self.assertFalse(self.user.has_module_perms('frontend'))

    def test_has_perm(self):
        self.assertTrue(self.user.has_perm('core.change_reimbursement'))
        self.assertFalse(self.user.has_perm('core.add_reimbursement'))
        self.assertFalse(self.user.has_perm('core.delete_reimbursement'))

from unittest.mock import Mock
from django.test import TestCase
from eventex.subscriptions.admin import SubscriptionModelAdmin
from eventex.subscriptions.admin import admin
from eventex.subscriptions.models import Subscription

class SubscriptionModelAdminTest(TestCase):

    def setUp(self):
        self.request = None
        self.model_admin = SubscriptionModelAdmin(Subscription, admin.site)
        self.obj = Subscription.objects.create(
                name='John Programmer',
                cpf='12345678901',
                email='john@example.com',
                phone='55-5555-5551')

    def test_has_action(self):
        """Action mark_as_paid should be installed."""
        self.assertIn('mark_as_paid', self.model_admin.actions)

    def test_mark_all(self):
        """It should mark all selected subscriptions as paid."""
        self.call_action()
        self.assertEqual(1, Subscription.objects.filter(paid=True).count())

    def test_message(self):
        """It should send a message to the user."""
        mock = self.call_action()
        message = '1 inscrição foi marcada como paga'
        mock.assert_called_once_with(self.request, message)

    def call_action(self):
        qs = Subscription.objects.all()

        mock = Mock()
        old_message_user = SubscriptionModelAdmin.message_user
        SubscriptionModelAdmin.message_user = mock

        self.model_admin.mark_as_paid(self.request, qs)

        SubscriptionModelAdmin.message_user = old_message_user

        return mock

import uuid

from datetime import datetime
from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
                name='John Programmer',
                cpf='12345678901',
                email='john@example.com',
                phone='55-5555-5551')
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto ``created_at`` attribute."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_hash_id(self):
        """Subscription must have an auto UUID4 ``hash_id`` attribute."""
        self.assertIsInstance(self.obj.hash_id, uuid.UUID)

    def test_str(self):
        self.assertEqual('John Programmer', str(self.obj))

    def test_paid_default_to_false(self):
        """By default, paid attribute must be False."""
        self.assertFalse(self.obj.paid)

from django.test import TestCase
from django.shortcuts import resolve_url as r

from eventex.subscriptions.models import Subscription


class SubscriptionDetailGet(TestCase):

    def setUp(self):
        self.obj = Subscription.objects.create(
                name='John Programmer',
                cpf='12345678901',
                email='john@example.com',
                phone='55-5555-5551'
            )
        url = r('subscriptions:detail', self.obj.hash_id)
        self.response = self.client.get(url)

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        template_name = 'subscriptions/subscription_detail.html'
        self.assertTemplateUsed(self.response, template_name)

    def test_context(self):
        subscription = self.response.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        contents = [
                self.obj.name,
                self.obj.cpf,
                self.obj.email,
                self.obj.phone,
            ]
        with self.subTest():
            for expected in contents:
                self.assertContains(self.response, expected)


class SubscriptionDetailNotFound(TestCase):

    def test_not_found(self):
        url = r('subscriptions:detail', '00000000-0000-0000-0000-000000000000')
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)

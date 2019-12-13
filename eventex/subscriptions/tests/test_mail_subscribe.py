from django.core import mail
from django.shortcuts import resolve_url as r
from django.test import TestCase


class SubscribePostValid(TestCase):

    def setUp(self):
        data = dict(
                name='John Programmer',
                cpf='12345678901',
                email='john@example.com',
                phone='55-5555-5551')
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = [
                'contato@eventex.com.br',
                'john@example.com',
            ]
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
                'John Programmer',
                '12345678901',
                'john@example.com',
                '55-5555-5551',
            ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

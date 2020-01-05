from django.test import TestCase
from django.shortcuts import resolve_url as r


class HomeTest(TestCase):
    fixtures = ['keynotes.json']

    def setUp(self):
        self.response = self.client.get(r('home'))

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use index.html template"""
        self.assertTemplateUsed(self.response, 'index.html')

    def test_subscription_link(self):
        """Response must contains subscription link"""
        expected = 'href="{}"'.format(r('subscriptions:new'))
        self.assertContains(self.response, expected)

    def test_speakers(self):
        """Must show keynote speakers"""
        contents = [
                'Grace Hopper',
                'http://hbn.link/hopper-pic',
                'href="{}"'.format(r('speaker_detail', slug='grace-hopper')),
                'Alan Turing',
                'http://hbn.link/turing-pic',
                'href="{}"'.format(r('speaker_detail', slug='alan-turing')),
            ]
        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)

    def test_speakers_link(self):
        """Must have a link to speakers section"""
        expected = 'href="{}#speakers"'.format(r('home'))
        self.assertContains(self.response, expected)

    def test_talks_link(self):
        """Must have a link to talks section"""
        expected = 'href="{}"'.format(r('talk_list'))
        self.assertContains(self.response, expected)

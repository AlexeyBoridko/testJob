"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from testTicketsApp.models import UserInfo
from django.test.client import Client
from django.core.urlresolvers import reverse

class SimpleTest(TestCase):

    fixtures = [
        'testTickets/testTicketsApp/fixtures/initial_data.json',
        ]

    def test_model(self):
        m = UserInfo.objects.get(pk=1)
        self.assertEqual(m.name, "Alexey")
        self.assertEqual(m.surname, "Boridko")
        self.assertEqual(m.email, "my@email.com")
        self.assertEqual(m.contacts, "Location - Kherson")


    def test_view(self):
        client = Client()
        response = client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<p>alexey@42cc.co</p>")

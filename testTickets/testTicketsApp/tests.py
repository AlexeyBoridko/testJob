from django.test import TestCase
from testTicketsApp.models import UserInfo
from django.test.client import Client
from django.core.urlresolvers import reverse
from  .models import MiddlewareRequests


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


    def test_db_for_requests_empty(self):
        emptyList = MiddlewareRequests.objects.all()
        self.assertEqual(emptyList.count(), 0)


    def test_request_object_create(self):
        MiddlewareRequests.objects.create(host="127.0.0.1:8000", path="/testonly/", method="GET")
        mList = MiddlewareRequests.objects.all()
        self.assertEqual(mList.count(), 1)

        m = MiddlewareRequests.objects.get(pk=1)
        self.assertEqual(m.host, "127.0.0.1:8000")
        self.assertEqual(m.path, "/testonly/")
        self.assertEqual(m.method, "GET")


    def test_request_tracker_middleware_full_cycle(self):
        client = Client()
        response = client.get(reverse('requests'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<td>/requests/</td>")


    def test_context_processor(self):
        client = Client()
        response = client.get(reverse('requests'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('django_settings' in response.context)
        self.assertIsNotNone(response.context['django_settings'])









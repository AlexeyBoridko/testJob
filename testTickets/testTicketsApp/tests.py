from django.test import TestCase
from testTicketsApp.models import UserInfo
from django.test.client import Client
from django.core.urlresolvers import reverse
from .models import MiddlewareRequests


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
        empty_list = MiddlewareRequests.objects.all()
        self.assertEqual(empty_list.count(), 0)

    def test_request_object_create(self):
        MiddlewareRequests.objects.create(host="127.0.0.1:8000", path="/testonly/", method="GET")
        records_list = MiddlewareRequests.objects.all()
        self.assertEqual(records_list.count(), 1)

        m = MiddlewareRequests.objects.get(pk=1)
        self.assertEqual(m.host, "127.0.0.1:8000")
        self.assertEqual(m.path, "/testonly/")
        self.assertEqual(m.method, "GET")

    def test_request_tracker_middleware_full_cycle(self):
        client = Client()
        response = client.get(reverse('requests'))
        records_list = MiddlewareRequests.objects.all()

        self.assertEqual(records_list.count(), 1)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<td>/requests/</td>")

    def test_first_10_requests_show(self):
        client = Client()
        for rec in range(15):
            client.get(reverse('requests'))

        response = client.get(reverse('requests'))

        requests_list = response.context['requestsList']
        self.assertEqual(requests_list.count(), 10)

        first_id = 1
        for rec in requests_list:
            self.assertEqual(rec.id, first_id)
            first_id += 1
from django.test import TestCase
from testTicketsApp.models import UserInfo
from django.test.client import Client
from django.core.urlresolvers import reverse
from .models import MiddlewareRequests


class SimpleTest(TestCase):
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

    def test_context_processor(self):
        client = Client()
        response = client.get(reverse('requests'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('django_settings' in response.context)
        self.assertIsNotNone(response.context['django_settings'])

    def test_edit_data(self):
        # get data
        user_info_id = UserInfo.objects.all()[0].id

        # First check edit form mast be present and login required
        client = Client()
        response = client.get(reverse('update', kwargs={'my_info_id': user_info_id}))

        #login required
        self.assertEqual(response.status_code, 302)

        #login
        response = client.login(username='alexey', password='alex')
        self.assertTrue(response, 'Login was unsuccessful')

        # now we will get edit page, because user is authenticated
        response = client.get(reverse('update', kwargs={'my_info_id': user_info_id}))
        self.assertEqual(response.status_code, 200)

        #checking update with correct new data
        ui = dict(name='name1', surname='surname1', date_of_birth='1980-01-10', contacts='contacts1',
                  email='some@mail.com', jid='wqw', skype_id='alex_', other_contacts='xd', bio='sd',
                  photo_file='')

        response = client.post(reverse('update', kwargs={'my_info_id': user_info_id}), ui)
        self.assertRedirects(response, reverse('main'))

        ui_changed = UserInfo.objects.get(pk=user_info_id)
        self.assertEqual(ui_changed.name, 'name1')

        #checking validation. Put incorrect new data to update post
        # surname field max_length = 50. Putting more
        ui["surname"] = "work phone number 12345678. home phone number 123456789000. Postcode 767544"

        response = client.post(reverse('update', kwargs={'my_info_id': user_info_id}), ui)
        self.assertContains(response, "Ensure this value has at most 50 characters (it has 75).")
        self.assertEqual(response.status_code, 200)

        #checking surname is not updated incorrect field value
        ui_changed = UserInfo.objects.get(pk=user_info_id)
        self.assertEqual(ui_changed.surname, 'surname1')

         #Checking email field on incorrect email format
        ui["surname"] = "surname1"
        ui["email"] = "email_test"

        response = client.post(reverse('update', kwargs={'my_info_id': user_info_id}), ui)
        self.assertContains(response, "Enter a valid email address.")
        self.assertEqual(response.status_code, 200)

        #Checking email field on correct email format
        ui["email"] = "alexey@mail.com"
        response = client.post(reverse('update', kwargs={'my_info_id': user_info_id}), ui)
        self.assertRedirects(response, reverse('main'))
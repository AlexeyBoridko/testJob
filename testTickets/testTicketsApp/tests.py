from StringIO import StringIO
from django.core.management import call_command
from django.test import TestCase
from testTicketsApp.models import UserInfo
from django.test.client import Client
from django.core.urlresolvers import reverse
from .models import MiddlewareRequests, ModelChangesLog
from testTicketsApp.templatetags.tags import edit_link


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
        response = client.login(username='admin', password='admin')
        self.assertTrue(response, 'Login was unsuccessful')

        # now we will get edit page, because user is authenticated
        response = client.get(reverse('update', kwargs={'my_info_id': user_info_id}))
        self.assertEqual(response.status_code, 200)

        #checking update with correct new data
        ui = dict(name='name1', surname='surname1', date_of_birth='12/01/1982', contacts='contacts1',
                  email='some@mail.com', jid='wqw', skype_id='alex_', other_contacts='xd', bio='sd')

        response_u = client.post(reverse('update', kwargs={'my_info_id': user_info_id}), ui,
                                 HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertRedirects(response_u, reverse('update', kwargs={'my_info_id': user_info_id}))
        uo = UserInfo.objects.get(pk=user_info_id)
        self.assertEqual(uo.name, ui["name"])

        #checking validation. Put incorrect new data to update post
        #Checking email field on incorrect email format
        ui["email"] = "email_test"

        resp = client.post(reverse('update', kwargs={'my_info_id': user_info_id}), ui,
                           HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertContains(resp, "Enter a valid email address")
        self.assertEqual(resp.status_code, 200)

        #Checking email field on correct email format
        ui["email"] = "alexeybor@mail.com"
        client.post(reverse('update', kwargs={'my_info_id': user_info_id}), ui, HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        ui_changed_email = UserInfo.objects.get(pk=user_info_id)
        self.assertEqual(ui_changed_email.email, ui["email"])

    def test_tag_edit_admin_(self):
        client = Client()
        response = client.get(reverse('main'))

        #check that we don't have access to edit by admin before login
        self.assertNotContains(response, "(admin)")

        #login
        response = client.login(username='admin', password='admin')
        self.assertTrue(response)

        #check again accesss to admin
        resp = client.get(reverse('main'))
        self.assertContains(resp, "(admin)")

        #check generated url
         # get data
        user_info_id = UserInfo.objects.all()[0].id
        self.assertEqual(edit_link(UserInfo.objects.all()[0]), '/admin/testTicketsApp/userinfo/%s/' % user_info_id)


    def test_print_models_command(self):
        obj = StringIO()
        call_command("printallmodels", stdout=obj)
        self.assertTrue('[UserInfo] - model has 1 object(s).' in obj.getvalue())


    def test_signals(self):
        #clean log
        obj_log = ModelChangesLog.objects.all()
        obj_log.delete()

        self.assertEqual(len(obj_log), 0)
        #let's update one record
        ci = UserInfo.objects.all()[0]
        ci.name = 'Alexey 1'
        ci.save()

        #make sure we have one update record
        obj = ModelChangesLog.objects.all()
        self.assertEqual(len(obj), 1)
        update_record = obj[0]
        self.assertEqual(update_record.action_type, 'updated')
        #let's delete the record
        ci.delete()
        obj = ModelChangesLog.objects.get(action_type='deleted')

        #let's check that model name equal ContactInfo
        self.assertEqual(obj.model_name, 'UserInfo')
        self.assertEqual(obj.action_type, 'deleted')


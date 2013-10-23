from django import forms
from models import UserInfo, MiddlewareRequests
from widgets import DateTimeWidget


class UserInfoForm(forms.ModelForm):
    #following fields need for setup additional html tags attributes on template page
    jid = forms.CharField(label='Jabber', max_length=50)
    skype_id = forms.CharField(label='Skype', max_length=50)
    other_contacts = forms.CharField(widget=forms.Textarea(attrs={'rows': 7, 'cols': 40}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'rows': 7, 'cols': 40}))
    photo = forms.ImageField(label='Photo', required=False, error_messages={'invalid': "Image files only"},
                             widget=forms.FileInput)
    date_of_birth = forms.DateTimeField(widget=DateTimeWidget(attrs={'readonly': ''},
                                                              options=dict(autoclose='true', minView='2', maxView='2')))


    class Meta:
        model = UserInfo
        fields = ['name', 'surname', 'date_of_birth', 'bio', 'email', 'jid',
                  'skype_id', 'other_contacts', 'contacts', 'photo']


    class Media:
        css = dict(all=('css/style.css',))
        js = ("js/jquery.form.js",)


class RequestsForm(forms.ModelForm):


     class Meta:
        model = MiddlewareRequests


     class Media:
        css = dict(all=('css/style.css',))
        js = ('js/jquery.latest.js', 'js/jquery.tablesorter.min.js')

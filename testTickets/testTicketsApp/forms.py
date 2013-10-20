from django import forms
from models import UserInfo
from widgets import DateTimeWidget


class UserInfoForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    surname = forms.CharField(max_length=50)
    jid = forms.CharField(max_length=50)
    skype_id = forms.CharField(max_length=50)
    contacts = forms.CharField(max_length=100)
    other_contacts = forms.CharField(widget=forms.Textarea(attrs={'rows': 7, 'cols': 40}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'rows': 7, 'cols': 40}))
    photo = forms.ImageField(label='Photo', required=False, error_messages={'invalid': "Image files only"},
                             widget=forms.FileInput)
    date_of_birth = forms.DateTimeField(widget=DateTimeWidget(attrs={'autoclose': 'true'}))

    class Meta(object):
        model = UserInfo
        fields = ['name', 'surname', 'date_of_birth', 'bio', 'email', 'jid',
                  'skype_id', 'other_contacts', 'contacts', 'photo']
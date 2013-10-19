from django import forms
from models import UserInfo


class UserInfoForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    surname = forms.CharField(max_length=50)
    jid = forms.CharField(max_length=50)
    skype_id = forms.CharField(max_length=50)
    contacts = forms.CharField(max_length=100)
    other_contacts = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 48}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 48}))
    photo = forms.ImageField(label='Photo', required=False, error_messages={'invalid': "Image files only"},
                             widget=forms.FileInput)

    class Meta(object):
        model = UserInfo
        fields = ['name', 'surname', 'date_of_birth', 'bio', 'email', 'jid',
                  'skype_id', 'other_contacts', 'contacts', 'photo']
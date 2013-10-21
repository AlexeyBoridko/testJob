from django import forms
from models import UserInfo


class UserInfoForm(forms.ModelForm):
    #following fields need for setup additional html tags attributes on template page
    jid = forms.CharField(label='Jabber', max_length=50)
    skype_id = forms.CharField(label='Skype', max_length=50)
    other_contacts = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 48}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 48}))
    photo = forms.ImageField(label='Photo', required=False, error_messages={'invalid': "Image files only"},
                             widget=forms.FileInput)

    class Meta(object):
        model = UserInfo
        fields = ['name', 'surname', 'date_of_birth', 'bio', 'email', 'jid',
                  'skype_id', 'other_contacts', 'contacts', 'photo']
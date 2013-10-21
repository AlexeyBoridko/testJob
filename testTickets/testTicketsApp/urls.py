from django.conf.urls import patterns, url
from testTickets import settings
from testTicketsApp import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
        url(r'^$', views.main, name='main'),
        url(r'^main/$', views.main, name='main'),
        url(r'^requests/$', views.requests_view, name='requests'),
        url(r'^login$', login, name='login'),
        url(r'^login(?P<next>.*)$', login),
        url(r'^logout/$', logout, {'next_page': '/main/'}, name="logout"),

        url(r'^(?P<my_info_id>\d+)/update/$', login_required(views.main_edit_update), name='update'),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
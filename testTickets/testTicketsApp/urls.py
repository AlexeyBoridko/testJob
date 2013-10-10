from django.conf.urls import patterns, url


from testTicketsApp import views


urlpatterns = patterns('',
        url(r'^$', views.main, name='main'),
)
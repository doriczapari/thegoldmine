from django.conf.urls import patterns, include, url
from . import views
from .views import MyRegistrationView

urlpatterns = patterns('',
    url(r'^$', views.home),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    url(r'postlist/$', views.post_list, name='post_list'),
    url(r'beginner/$', views.post_beginner_list, name='post_beginner_list'),
    url(r'intermediate/$', views.post_intermediate_list, name='post_intermediate_list'),
    url(r'advanced/$', views.post_advanced_list, name='post_advanced_list'),
    url(r'general/$', views.post_general_list, name='post_general_list'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^search/*$', views.post_search, name='post_search'),
    url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),

    #url(r'^users/(?P<slug>\w+)/$', UserProfileDetailView.as_view(), name="profile"),
)

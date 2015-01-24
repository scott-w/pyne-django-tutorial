from django.conf.urls import patterns, url

from chatter.base.views import ChatListView


urlpatterns = patterns(
    '',
    url(r'^$', ChatListView.as_view()),
)

from django.conf.urls import patterns, url

from chatter.base.views import ChatListView, UserChatListView


urlpatterns = patterns(
    '',
    url(r'^$', ChatListView.as_view(), name='index'),
    url(r'^@(?P<username>.+)/$', UserChatListView.as_view(), name='chat-user')
)

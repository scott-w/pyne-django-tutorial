from django.conf.urls import patterns, url

from chatter.base.views import ChatCreateView, ChatListView, UserChatListView


urlpatterns = patterns(
    '',
    url(r'^$', ChatListView.as_view(), name='index'),
    url(r'^@(?P<username>.+)/$', UserChatListView.as_view(), name='chat-user'),
    url(r'^new/$', ChatCreateView.as_view(), name='chat-create'),
)

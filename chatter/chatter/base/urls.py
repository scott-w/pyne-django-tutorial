from django.conf.urls import url

from chatter.base.views import ChatViewSet


urlpatterns = (
    url(
        r'^$',
        ChatViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='chat-list'
    ),
)

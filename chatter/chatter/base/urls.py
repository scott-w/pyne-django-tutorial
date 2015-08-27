from django.conf.urls import url

from rest_framework.authtoken import views as tokenviews

from chatter.base.views import ChatViewSet


urlpatterns = (
    url(
        r'^$',
        ChatViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='chat-list'
    ),
    url(r'^tokens/', tokenviews.obtain_auth_token)

)

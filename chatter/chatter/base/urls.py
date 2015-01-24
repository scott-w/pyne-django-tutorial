from django.conf.urls import patterns, url

from chatter.base.views import ChatListView


urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'chatter.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', ChatListView.as_view()),
)

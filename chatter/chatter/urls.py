from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chatter.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

# The documentation for authentication views can be found at:
# https://docs.djangoproject.com/en/1.7/topics/auth/default/#module-django.contrib.auth.views
urlpatterns += patterns('django.contrib.auth.views',
    url(r'^login/$', 'login', name='login'),
    url(r'^logout/$', 'logout_then_login', name='logout'),
    url(r'^reset/$', 'password_reset', name='password_reset'),
    url(r'^reset/done/$', 'password_reset_done', name='password_reset_done'),
    url(
        r'^reset/confirm/'
        r'(?P<uidb64>[0-9A-Za-z_\-]+)/'
        r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'password_reset_confirm',
        name='password_reset-confirm'),
    url(
        r'^reset/complete/$',
        'password_reset_complete',
        name='password_reset_complete'),
)

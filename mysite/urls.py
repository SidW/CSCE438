from django.conf.urls import patterns, include, url
from views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^test/$', test),

    url(r'^admin/', include(admin.site.urls)),

    #user auth urls
    url(r'^accounts/login/$', login),
    url(r'^accounts/auth/$', auth_view),
    url(r'^accounts/logout/$', logout),
    url(r'^accounts/loggedin/$', loggedin),
    url(r'^accounts/invalid/$', invalid_login),
    url(r'^accounts/register/$', register_user),
    url(r'^accounts/register_success/$', register_success),


    url(r'^hello/$', hello),
   # url('^time/$', current_datetime),
   # url(r'^time/plus/(\d{1,2})/$', hours_ahead)
)

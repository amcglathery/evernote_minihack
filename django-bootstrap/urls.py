from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'base.views.index'),
    url(r'^login/$', 'account.views.login_page'),
    url(r'^auth/gettok/$', 'base.views.run_evernote_auth'),
    url(r'^auth/login/$', 'base.views.login_evernote_token'),
    url(r'^auth/logout/$', 'account.views.logout_page'),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
            url(r'^static/(?P<path>.*)$', 'serve'),
    )

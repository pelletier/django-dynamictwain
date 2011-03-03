from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^testproj/', include('testproj.foo.urls')),

    (r'^twain/', include('dynamictwain.urls')),


    (r'^foobar/$', 'testme.views.foo'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)

from django.conf import settings
from os import path

if settings.DEBUG:
    # Media URLs
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': path.join(path.dirname(__file__), "site_media")}),
    )


from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'scan/$', 'dynamictwain.views.scan', name='scan'),
    url(r'upload/$', 'dynamictwain.views.upload', name='upload'),
)

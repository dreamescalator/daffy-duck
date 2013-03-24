from django.conf.urls import patterns, url
from ship.views import home, worker, add_new_pkg, logout, add_new_recipient

urlpatterns = patterns('',
                       url(r'^$', home),
                       url(r'^worker/', worker),
                       url(r'^create-new-package/', add_new_pkg),
                       url(r'^create-new-recipient', add_new_recipient),
                       url(r'^logout/', logout),
                      
                       )
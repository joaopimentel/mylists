from django.conf.urls import patterns, include, url

from django.contrib import admin

from listapp.views import LinkList

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', LinkList.as_view()),
)

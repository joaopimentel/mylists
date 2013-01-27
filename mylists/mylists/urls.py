from django.conf.urls import patterns, include, url

from django.contrib import admin

from listapp.views import LinkList, category_detail, CategoryList
from mailfetcher.views import get_links

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/login/', 'django.contrib.auth.views.login',
        name="login"),
    url(r'^accounts/logout/', 'django.contrib.auth.views.logout_then_login',
        name="logout"),

    url(r'^$', LinkList.as_view()),
    url(r'^links/$', LinkList.as_view(),
        name="link_list"),

    url(r'^tag/(?P<tag>\w+)/$', category_detail,
        name="category_detail"),
    url(r'^tag/$', CategoryList.as_view(),
        name="category_list"),

    url(r'^fetch/', get_links),
)

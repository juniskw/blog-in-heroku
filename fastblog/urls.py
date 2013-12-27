#!/usr/bin/env python
#coding:utf-8

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('fastblog.page_of_fastblog.views',
    # Examples:
    # url(r'^$', 'fastblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	 url( r'^new/$','new' ),	# view関数はincludeしない！
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

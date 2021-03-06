#!/usr/bin/env python
#coding:utf-8

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('fastblog.page_of_fastblog.views',
    # Examples:
    # url(r'^$', 'fastblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	 
	 url( r'^$','top_page',name='Blog' ),
	 url( r'^new/$','new',name='New' ),	# view関数はincludeしない！
	 url( r'^(?P<entry_id>\d+)/edit/$','edit',name='Edit' ),
	 url( r'^(?P<entry_id>\d+)/delete/$','delete',name='Delete' ),
	 url( r'^login/$','log_in',name='Login' ),
	 url( r'^logout/$','log_out',name='Logout' ),
)

urlpatterns += patterns('',
    url( r'^admin/', include(admin.site.urls) ),
	 #url( r'^login/$','django.contrib.auth.views.login',name='Login' ),
	 #url( r'^logout/$','log_out',name='Logout' ),
)

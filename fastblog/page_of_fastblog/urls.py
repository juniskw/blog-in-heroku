#coding:utf-8

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
	# url(r'^$', 'fastblog.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	#url( r'^$',include('views.top_page') ),
)


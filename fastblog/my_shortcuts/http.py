#!/usr/bin/env python
#coding:utf-8

def response_view(req,path_to_temp,contxt_dic):
	from django.http import HttpResponse
	from django.template import loader,RequestContext,Context

	template = loader.get_template(path_to_temp)
	context = RequestContext(req,contxt_dic)

	return HttpResponse( template.render(context) )


def redirect(url):
	from django.http import HttpResponseRedirect

	return HttpResponseRedirect(url)

#!/usr/bin/env python
#coding:utf-8

def login_check(func):
	from django.http import HttpResponseRedirect

	def new_func(req,entry_id=None):
		if req.user.is_authenticated():
			if entry_id is None:
				return func(req)
			else:
				return func(req,entry_id)
		else:
			return HttpResponseRedirect('/login?next=%s' % req.path)

	return new_func

#coding:utf-8

from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader,RequestContext,Context
from django.contrib.auth import authenticate	#
#from django.contrib.auth.decorators import login_required	#

def top_page(req):
	from fastblog.page_of_fastblog.models import Entry
	rows = Entry.objects.all().order_by('-create_datetime')

	contexts = RequestContext(req,{
		'rows':rows,
		'user':req.user,
	})
	template = loader.get_template('page_of_fastblog/index.html')
	return HttpResponse( template.render(contexts) )

#@login_required	#
def new(req):

	if req.user.is_authenticated():
	
		from fastblog.page_of_fastblog.forms import EntryForm

		if req.method == 'POST':
			form = EntryForm(req.POST)
		else:
			form = EntryForm()

		if form.is_valid():	# 入力チェック
			from fastblog.page_of_fastblog.models import Entry

			new_entry = Entry()

			new_entry.title = form.cleaned_data['title']	# form.cleaned_data['name']はフォーム値の取得。それをモデルに渡している。
			new_entry.body = form.cleaned_data['body']

			new_entry.owner = req.user	#

			new_entry.save()

			return HttpResponseRedirect('/')

		contexts = RequestContext(req,{
			'form':form,
			'posted':req.method=='POST',
		})

		template = loader.get_template('page_of_fastblog/new.html')

		return HttpResponse( template.render(contexts) )

	else:

		return HttpResponseRedirect('/login/?next=%s' % req.path)

#@login_required	#
def edit(req,entry_id):

	from django.http import Http404

	try:
		from fastblog.page_of_fastblog.models import Entry

		entry = Entry.objects.get(pk=entry_id)

	except Entry.DoesNotExist:
		raise Http404

	if req.user.is_authenticated():
		if req.user == entry.owner:

			if req.method == 'POST':
				form = req.POST

				if (form['title']!=entry.title) or (form['body']!=entry.body):	
		# どちらかが変更されていたら・・・

					entry.title = form['title']
					entry.body = form['body']

					entry.save()

					return HttpResponseRedirect('/')

		else:

			return HttpResponse("Bad request")
	
		contexts = RequestContext(req,{
			'title':entry.title,
			'body':entry.body,
			'request':req,
		})
		template = loader.get_template('page_of_fastblog/edit.html')

		return HttpResponse( template.render(contexts) )

	else:

		return HttpResponseRedirect('/login/?next=%s' % req.path)

#@login_required	#
def delete(req,entry_id):
	from django.http import Http404

	try:
		from fastblog.page_of_fastblog.models import Entry

		entry = Entry.objects.get(pk=entry_id)

	except Entry.DoesNotExist:
		raise Http404

	if req.user.is_authenticated():
		if req.user == entry.owner:

			if req.method == 'POST':
				entry.delete()
				return HttpResponseRedirect('/')
		
			template = loader.get_template('page_of_fastblog/delete.html')
			contexts = RequestContext(req,{
				'title':entry.title,
				'body':entry.body,
				'create':entry.create_datetime,
				'update':entry.update_datetime,
			})

			return HttpResponse( template.render(contexts) )

		else:
			return HttpResponse("Bad request")

	else:
		return HttpResponseRedirect('/login/?next=%s' % req.path)


def log_in(req):
	from django.contrib.auth import login

	if req.method=='POST':
		uname = req.POST['username']
		pword = req.POST['password']
		user = authenticate( username=uname,password=pword )

		if user is not None:
			if user.is_active:

				login(req,user)

				return HttpResponseRedirect('/')	#go to next

			else:

				return HttpResponse("Error: account is not active...")	#

		else:
	
			return HttpResponse("Error: login was failed...,Please retry")	#

	else:
		template = loader.get_template('page_of_fastblog/login.html')
		contexts = RequestContext(req,{})

		return HttpResponse( template.render(contexts) )

def log_out(req):
	from django.contrib.auth import logout
	logout(req)

	return HttpResponseRedirect('/')

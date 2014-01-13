#coding:utf-8

from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader,RequestContext,Context
from django.contrib.auth import authenticate	#
from fastblog.my_shortcuts.http import response_view,redirect
from fastblog.my_shortcuts.auth import login_check
#from django.contrib.auth.decorators import login_required	#


def top_page(req):
	from fastblog.page_of_fastblog.models import Entry
	rows = Entry.objects.all().order_by('-create_datetime')

	return response_view(req,'page_of_fastblog/index.html',{
		'rows':rows,
		'user':req.user,
	})


@login_check
def new(req):

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

		return redirect('/')

	return response_view(req,'page_of_fastblog/new.html',{
		'form':form,
		'posted':req.method=='POST',
	})


@login_check
def edit(req,entry_id):

	from django.http import Http404

	try:
		from fastblog.page_of_fastblog.models import Entry

		entry = Entry.objects.get(pk=entry_id)

	except Entry.DoesNotExist:
		raise Http404

	if req.user == entry.owner:

		if req.method == 'POST':
			form = req.POST

			if (form['title']!=entry.title) or (form['body']!=entry.body):	
		# どちらかが変更されていたら・・・

				entry.title = form['title']
				entry.body = form['body']

				entry.save()

				return redirect('/')

	else:

		return HttpResponse("Bad request")
	
	return response_view(req,'page_of_fastblog/edit.html',{
		'title':entry.title,
		'body':entry.body,
		'request':req,
	})


@login_check
def delete(req,entry_id):
	from django.http import Http404

	try:
		from fastblog.page_of_fastblog.models import Entry

		entry = Entry.objects.get(pk=entry_id)

	except Entry.DoesNotExist:
		raise Http404

	if req.user == entry.owner:

		if req.method == 'POST':
			entry.delete()
			return redirect('/')
		
		return response_view(req,'page_of_fastblog/delete.html',{
			'title':entry.title,
			'body':entry.body,
			'create':entry.create_datetime,
			'update':entry.update_datetime,
		})

	else:
		return HttpResponse("Bad request")


def log_in(req):
	from django.contrib.auth import login

	user = req.user

	if user.is_authenticated():
		return redirect('/')	# ログイン済みならトップページに

	else:
		if req.method=='POST':
			uname = req.POST['username']
			pword = req.POST['password']
			user = authenticate( username=uname,password=pword )

			if user is not None:
				if user.is_active:

					login(req,user)

					return redirect(req.GET['next'])

				else:
					pass

			else:
				pass

		return response_view(req,'page_of_fastblog/login.html',{
			'request':req.method,
			'user':user,
		})


def log_out(req):
	from django.contrib.auth import logout
	logout(req)

	return response_view(req,'page_of_fastblog/logout.html',{})

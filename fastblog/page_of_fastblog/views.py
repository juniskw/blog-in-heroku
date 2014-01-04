#coding:utf-8

from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader,RequestContext,Context


def top_page(req):
	from fastblog.page_of_fastblog.models import Entry
	rows = Entry.objects.all().order_by('-create_datetime')

	contexts = RequestContext(req,{
		'rows':rows,
	})
	template = loader.get_template('page_of_fastblog/index.html')
	return HttpResponse( template.render(contexts) )

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

		new_entry.save()

		return HttpResponseRedirect('/')

	contexts = RequestContext(req,{
		'form':form,
	})

	template = loader.get_template('page_of_fastblog/new.html')

	return HttpResponse( template.render(contexts) )


def edit(req,entry_id):
	from django.http import Http404
	try:
		from fastblog.page_of_fastblog.models import Entry
		entry = Entry.objects.get(pk=entry_id)
	except Entry.DoesNotExist:
		raise Http404
	
	if req.method == 'POST':
		form = req.POST

		if (form['title']!=entry.title) or (form['body']!=entry.body):	
		# どちらかが変更されていたら・・・

			entry.title = form['title']
			entry.body = form['body']

			entry.save()

			return HttpResponseRedirect('/')
	
	contexts = RequestContext(req,{
		'title':entry.title,
		'body':entry.body,
	})
	template = loader.get_template('page_of_fastblog/edit.html')

	return HttpResponse( template.render(contexts) )


def delete(req,entry_id):
	pass

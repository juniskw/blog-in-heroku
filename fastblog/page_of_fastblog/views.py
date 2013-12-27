#coding:utf-8

from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader,RequestContext

# from django.shortcuts import render

def new(req):
	from fastblog.page_of_fastblog.forms import EntryForm

	if req.method == 'POST':
		form = EntryForm(req.POST)
	else:
		form = EntryForm()

	if form.is_valid():	# 入力チェック
		from page_of_fastblog.models import Entry

		new_entry = Entry()

		new_entry.title = form.cleaned_data['title']	# form.cleaned_data['name']はフォーム値の取得。それをモデルに渡している。
		new_entry.body = forms.cleaned_data['body']

		new_entry.save()

		return HttpResponseRedirect('/')

	contexts = RequestContext(req,{
		'form':form,
	})

	template = loader.get_template('page_of_fastblog/new.html')

	return HttpResponse( template.render(contexts) )

"""
def top_page():
	pass
"""
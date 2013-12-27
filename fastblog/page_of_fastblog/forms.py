#coding:utf-8

from django import forms

class EntryForm(forms.Form):
	title = forms.CharField(
		label = u'題名',
	)

	body = forms.CharField(
		label = u'本文',
		widget = forms.Textarea(),
	)

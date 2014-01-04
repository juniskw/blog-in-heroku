#coding:utf-8

from django import forms

class EntryForm(forms.Form):
	title = forms.CharField(
		initial = '',
		label = u'題名',
		widget = forms.TextInput( attrs={'class':"form-control",} ),
	)
	def __unicode__(self):
		return self.title

	body = forms.CharField(
		label = u'本文',
		widget = forms.Textarea( attrs={'class':"form-control",'rows':"5",} ),
	)

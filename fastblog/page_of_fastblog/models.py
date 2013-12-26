from django.db import models

class Entry(models.Model):
	title = models.CharField(max_length=150)
	body = models.TextField()
	create_datetime = models.DateTimeField(auto_now_add=True)
	update_datetime = models.DateTimeField(auto_now=True)

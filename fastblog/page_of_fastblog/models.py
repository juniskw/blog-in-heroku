from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):
	title = models.CharField(max_length=150)
	body = models.TextField()
	create_datetime = models.DateTimeField(auto_now_add=True)
	update_datetime = models.DateTimeField(auto_now=True)
	owner = models.ForeignKey(User)

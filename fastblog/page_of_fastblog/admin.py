from django.contrib import admin

from fastblog.page_of_fastblog import models

class EntryAdmin(admin.ModelAdmin):
	list_display = ('id','title')

admin.site.register(models.Entry,EntryAdmin)

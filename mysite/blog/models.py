from django.db import models
from django.contrib import admin

# Create your models here.
class BlogPost(models.Model):
	titulo = models.CharField(max_length=150)
	body = models.TextField()
	timestamp = models.DateTimeField()
	# postak ordenaitteko barrixenetik zarrenera
	class Meta:
		ordering = ('-timestamp',)

class BlogPostAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'timestamp')

admin.site.register(BlogPost, BlogPostAdmin)
from django.contrib import admin

# Register your models here.

# Comment model

from .models import NewsStory, Comment

admin.site.register(NewsStory)
admin.site.register(Comment)

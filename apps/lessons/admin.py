from django.contrib import admin

from .models import Category, Lesson, WatchHistory

admin.site.register(Category)
admin.site.register(Lesson)
admin.site.register(WatchHistory)
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from newspaper.models import Topic, Article, Tag

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'creator']}),
        ('Article body', {'fields':['body','tags', 'topic']})
    ]
    list_display=['name','creator', 'created', 'topic']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display=['name']    
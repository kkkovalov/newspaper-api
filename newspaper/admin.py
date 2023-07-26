from django.contrib import admin
from . import models

# Models view
class CreatorAdmin(admin.ModelAdmin):
    pass

class ReaderAdmin(admin.ModelAdmin):
    pass

class TopicAdmin(admin.ModelAdmin):
    pass

class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'creator']}),
        ('Article body', {'fields':['body','tags', 'topic']})
    ]
    list_display=['name','creator', 'created', 'topic']

class TagAdmin(admin.ModelAdmin):
    list_display=['name']

# Register your models here.
admin.site.register(models.Creator, CreatorAdmin)
admin.site.register(models.Reader, ReaderAdmin)
admin.site.register(models.Topic, TopicAdmin)
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Tag, TagAdmin)

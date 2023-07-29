from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . import models

# Models view

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'last_login')}),
        ('Permissions', {'fields': ('is_active','is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )
    
    list_display = ('email', 'is_staff', 'last_login')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

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

# Register your models here
admin.site.register(models.Topic, TopicAdmin)
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.User, UserAdmin)

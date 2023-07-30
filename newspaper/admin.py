from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from newspaper.models import Topic, Article, Tag, User

# Models view
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'last_login')}),
        ('Permissions', {'fields': ('is_active','date_joined','is_staff', 'is_superuser', 'groups', 'user_permissions')}),
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
    
    list_display = ('email', 'is_staff', 'last_login', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


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
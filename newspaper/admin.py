from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from newspaper.models import Topic, Article, Tag, User

# Models view

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
admin.site.register(Topic, TopicAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(User, UserAdmin)

from django.contrib import admin
from .models import Guideline, Comment

# admin.site.register(Guideline)


@admin.register(Guideline)
class GuideAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date', 'status')
    list_filter = ('status', 'created_date', 'publish_date', 'author')
    search_fields = ('title', 'text')
    raw_id_fields = ('author',)
    date_hierarchy = 'publish_date'
    ordering = ('status', 'publish_date')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'guideline', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')





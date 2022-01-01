from django.contrib import admin
from django.db.models.aggregates import Count
from django_summernote.admin import SummernoteModelAdmin
from . import models


@admin.register(models.Profile)
class ProfileAdmin(SummernoteModelAdmin):
    list_display = ['first_name', 'last_name']
    list_per_page = 10
    summernote_fields = ['bio']


@admin.register(models.Blog)
class BlogAdmin(SummernoteModelAdmin):
    list_display = ['title']
    list_filter = ['tags', 'blog_date']
    list_per_page = 10
    autocomplete_fields = ['tags']
    summernote_fields = ['body']

    prepopulated_fields = {
        'slug': ['title']
    }


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name__istartswith']


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'received_at']


@admin.register(models.Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['name']

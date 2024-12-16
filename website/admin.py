from django.contrib import admin
from django.utils.html import format_html

# Register your models here.

from . models import *

@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'email', 'phone', 'address')
    prepopulated_fields = {'slug': ('name',)}
    
    
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'sub_title')
    prepopulated_fields = {'slug': ('title',)}
    
    
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'sub_title')
    prepopulated_fields = {'slug': ('title',)}
    
    
@admin.register(PageChild)
class PageChildAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'sub_title')
    prepopulated_fields = {'slug': ('title',)}
    
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
    
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'show_image')
    prepopulated_fields = {'slug': ('title',)}
    
    def show_image(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" width="100"  />')
        return 'No image'
    
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message')
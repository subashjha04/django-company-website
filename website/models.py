from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Settings(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='logo/', blank=True, null=True)
    fabicon = models.ImageField(upload_to='fabicon/', blank=True, null=True)
    meta_title = models.CharField(max_length=100, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    
    
    def __str__(self):
        return self.name


class Page(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    sub_title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='page/', blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    meta_title = models.CharField(max_length=100, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    page_section_name = models.CharField(max_length=100, blank=True, null=True)
    

class Service(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    sub_title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='service/', blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    meta_title = models.CharField(max_length=100, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    
    @property
    def get_limit_summary(self):
        return self.summary[:100] + '...'
    
    
    
class PageChild(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    sub_title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='page/', blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    
    
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    
    
class Blog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    sub_title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    meta_title = models.CharField(max_length=100, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    
    
    @property
    def get_limit_summary(self):
        return self.summary[:170] + '...'
    
    
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
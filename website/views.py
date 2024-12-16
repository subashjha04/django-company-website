from django.shortcuts import render
from .models import *
from .contact_form import ContactForm
import requests

# Create your views here.


def index(request):
    data={
        'aboutus': Page.objects.get(page_section_name='about-us'),
        'serviceData': Service.objects.order_by('-id')[:4],
        'blogData': Blog.objects.order_by('-id')[:3],
    }
    return render(request, 'index.html', data)


def about(request):
    data={
        'aboutus': Page.objects.get(page_section_name='about-us'),

    }
    return render(request, 'about.html', data)

def service_views(request):
    data={
        'serviceData': Service.objects.all,
    }
    return render(request, 'service.html', data)


def service_details(request, slug):
    data={
        'serviceData': Service.objects.get(slug=slug),
    }
    return render(request, 'service_details.html', data)


def blog_views(request):
    data={
        'blogData': Blog.objects.all,
    }
    return render(request, 'blog.html', data)


def blog_details(request, slug):
    data={
        'blogData': Blog.objects.get(slug=slug),
    }
    return render(request, 'blog-details.html', data)


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact.html', {'contactForm': ContactForm(), 'msg': 'Your message has been sent successfully'})
        else:
            return render(request, 'contact.html', {'contactForm': form})
    else:
        data={
            'contactForm': ContactForm(),
        }
    return render(request, 'contact.html', data)


def api_news(request):
    url = "https://newsapi.org/v2/everything?q=tesla&from=2024-11-16&sortBy=publishedAt&apiKey=692de9de0d464ec4b6684772e4672497"
    response = requests.get(url)
    news_data = response.json()
    data = {
        'newsData': news_data['articles']
    }
    return render(request, 'api-news.html', data)
from django.shortcuts import render
from .models import Entry

def index(request):
    latest_blog_list = Entry.objects.order_by('-pub_date')[:5]
    template = 'blogs/index.html'
    context = {
        'latest_blog_list': latest_blog_list,
    }
    return render(request, template, context)

def detail(request, entry_id):
    entry = Entry.objects.get(pk=entry_id)
    template = 'blogs/detail.html'
    context = {
        'entry': entry,
    }
    return render(request, template, context)

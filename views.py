from django.shortcuts import render, get_object_or_404
from .models import Page


def index(request):
    return render(request, 'mainstay_wiki/index.html')


def page(request, title):
    page_ = get_object_or_404(Page, title=title)
    context = {'page': page_}
    return render(request, 'mainstay_wiki/page.html', context)

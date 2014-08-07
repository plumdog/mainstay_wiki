from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Page
from .forms import PageForm


RECENT = 10

def index(request):
    recently_updated = Page.objects.order_by('-updated_at').all()[:RECENT]
    return render(request, 'mainstay_wiki/index.html', {'recently_updated': recently_updated})


def page(request, title):
    page_ = get_object_or_404(Page, title=title)
    context = {'page': page_}
    return render(request, 'mainstay_wiki/page.html', context)


def add_page(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Page added')
            return redirect('mainstay_wiki:index')
        else:
            messages.error(request, 'Errors')
    else:
        form = PageForm()

    return render(request, 'mainstay_wiki/add.html', {'form': form})


def edit_page(request, title):
    page_ = get_object_or_404(Page, title=title)
    if request.method == 'POST':
        form = PageForm(request.POST, instance=page_)
        if form.is_valid():
            form.save()
            messages.success(request, 'Page editted')
            return redirect('mainstay_wiki:page', page_.title)
        else:
            messages.error(request, 'Errors')
    else:
        form = PageForm(instance=page_)

    return render(request, 'mainstay_wiki/edit.html', {'form': form})

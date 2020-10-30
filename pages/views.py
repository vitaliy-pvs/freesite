from django.shortcuts import render, get_object_or_404
from .models import Page


def main_page(request):
    page = get_object_or_404(Page, title='mainpage')
    return render(request, 'page.html', {'page': page})


def page_by_pk(request, pk):
    page = get_object_or_404(Page, pk=pk)
    return render(request, 'page.html', {'page': page})


def page_by_title(request, title):
    page = get_object_or_404(Page, title=title)
    return render(request, 'page.html', {'page': page})


def site_map(request):
    pages = Page.objects.all()
    return render(request, 'site_map.html', {'pages': pages})

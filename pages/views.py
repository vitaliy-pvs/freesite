from django.shortcuts import render, get_object_or_404
from .models import Page


def show_page(request, pk):
    page = get_object_or_404(Page, pk=pk)
    return render(request, 'page.html', {'page': page})


def main_page(request):
    page = get_object_or_404(Page, number=0)
    return render(request, 'page.html', {'page': page})


def site_map(request):
    pages = Page.objects.all()
    return render(request, 'site_map.html', {'pages': pages})

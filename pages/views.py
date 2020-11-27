import os

from django.shortcuts import render, get_object_or_404, redirect

from freesite.settings import STATIC_ROOT
from .models import Page, MenuPage, Settings


favicon_path = "#"
if os.path.isfile(os.path.join(STATIC_ROOT, 'favicon.png')):
    favicon_path = "static/favicon.png"

logo_exists = False
if os.path.isfile(os.path.join(STATIC_ROOT, 'logo.png')):
    logo_exists = True

header_path = "#"
if os.path.isfile(os.path.join(STATIC_ROOT, 'header.png')):
    header_path = "static/header.png"


def menu_page(request, pk):
    settings = Settings.objects.all()
    menu_pages = MenuPage.objects.order_by('number')
    page = get_object_or_404(MenuPage, pk=pk)
    if page.title == settings[0].main_page_title:
        return redirect('main_page')
    if page.title == settings[0].page_list_title:
        return redirect('page_list')
    return render(request, 'page.html', {
        'menu_pages': menu_pages,
        'page': page,
        'settings': settings[0],
        'favicon_path': favicon_path,
        'logo_exists': logo_exists,
        'header_path': header_path
    })


def page_list(request):
    settings = Settings.objects.all()
    menu_pages = MenuPage.objects.order_by('number')
    pages = Page.objects.all()
    return render(request, 'page_list.html', {
        'menu_pages': menu_pages,
        'pages': pages,
        'settings': settings[0],
        'favicon_path': favicon_path,
        'logo_exists': logo_exists,
        'header_path': header_path
    })


def main_page(request):
    settings = Settings.objects.all()
    menu_pages = MenuPage.objects.order_by('number')
    page = get_object_or_404(MenuPage, title=settings[0].main_page_title)
    return render(request, 'page.html', {
        'menu_pages': menu_pages,
        'page': page,
        'settings': settings[0],
        'favicon_path': favicon_path,
        'logo_exists': logo_exists,
        'header_path': header_path
    })


def page(request, pk):
    settings = Settings.objects.all()
    menu_pages = MenuPage.objects.order_by('number')
    page = get_object_or_404(Page, pk=pk)
    return render(request, 'page.html', {
        'menu_pages': menu_pages,
        'page': page,
        'settings': settings[0],
        'favicon_path': favicon_path,
        'logo_exists': logo_exists,
        'header_path': header_path
    })


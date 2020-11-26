from django.shortcuts import render, get_object_or_404, redirect
from .models import Page, MenuPage, Settings
import os.path
from os import path

PROJECT_PATH = path.realpath(path.dirname(__file__))

favicon_path = "#"
if os.path.isfile(PROJECT_PATH + "/static/favicon.png"):
    favicon_path = "static/favicon.png"

logo_path = "#"
if os.path.isfile(PROJECT_PATH + "/static/logo.png"):
    logo_path = "static/logo.png"

header_path = "#"
if os.path.isfile(PROJECT_PATH + "/static/header.png"):
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
        'logo_path': logo_path,
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
        'logo_path': logo_path,
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
        'logo_path': logo_path,
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
        'logo_path': logo_path,
        'header_path': header_path
    })


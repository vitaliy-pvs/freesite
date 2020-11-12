from django.shortcuts import render, get_object_or_404, redirect
from .models import Page, MenuPage, Settings


def main_page(request):
    settings = Settings.objects.all()
    menu_pages = MenuPage.objects.order_by('number')
    page = get_object_or_404(Page, title='mainpage')
    return render(request, 'page.html', {'menu_pages': menu_pages, 'page': page, 'settings': settings[0]})


def page(request, pk):
    settings = Settings.objects.all()
    menu_pages = MenuPage.objects.order_by('number')
    page = get_object_or_404(Page, pk=pk)
    return render(request, 'page.html', {'menu_pages': menu_pages, 'page': page, 'settings': settings[0]})


def menu_page(request, pk):
    settings = Settings.objects.all()
    menu_pages = MenuPage.objects.order_by('number')
    page = get_object_or_404(MenuPage, pk=pk)
    if page.title == "Главная":
        return redirect('/')
    if page.title == "Карта сайта":
        return redirect('site_map')
    return render(request, 'page.html', {'menu_pages': menu_pages, 'page': page, 'settings': settings[0]})


def site_map(request):
    settings = Settings.objects.all()
    menu_pages = MenuPage.objects.order_by('number')
    pages = Page.objects.all()
    return render(request, 'site_map.html', {'menu_pages': menu_pages, 'pages': pages, 'settings': settings[0]})

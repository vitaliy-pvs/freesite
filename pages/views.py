from django.shortcuts import render, get_object_or_404, redirect
from .models import Page, MenuPage


def main_page(request):
    menu_pages = MenuPage.objects.order_by('number')
    page = get_object_or_404(Page, title='mainpage')
    return render(request, 'page.html', {'menu_pages': menu_pages, 'page': page})


def page(request, pk):
    menu_pages = MenuPage.objects.order_by('number')
    page = get_object_or_404(Page, pk=pk)
    return render(request, 'page.html', {'menu_pages': menu_pages, 'page': page})


def menu_page(request, pk):
    menu_pages = MenuPage.objects.order_by('number')
    page = get_object_or_404(MenuPage, pk=pk)
    if page.title == "Главная":
        return redirect('/')
    return render(request, 'page.html', {'menu_pages': menu_pages, 'page': page})


def site_map(request):
    menu_pages = MenuPage.objects.order_by('number')
    pages = Page.objects.all()
    return render(request, 'site_map.html', {'menu_pages': menu_pages, 'pages': pages})

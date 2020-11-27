from django.shortcuts import render, get_object_or_404, redirect

from .models import Page, MenuPage, Settings


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
        'settings': settings[0]
    })


def page_list(request):
    settings = Settings.objects.all()
    menu_pages = MenuPage.objects.order_by('number')
    pages = Page.objects.all()
    return render(request, 'page_list.html', {
        'menu_pages': menu_pages,
        'pages': pages,
        'settings': settings[0]
    })


def main_page(request):
    settings = Settings.objects.all()
    menu_pages = MenuPage.objects.order_by('number')
    page = get_object_or_404(MenuPage, title=settings[0].main_page_title)
    return render(request, 'page.html', {
        'menu_pages': menu_pages,
        'page': page,
        'settings': settings[0]
    })


def page(request, pk):
    settings = Settings.objects.all()
    menu_pages = MenuPage.objects.order_by('number')
    page = get_object_or_404(Page, pk=pk)
    return render(request, 'page.html', {
        'menu_pages': menu_pages,
        'page': page,
        'settings': settings[0]
    })


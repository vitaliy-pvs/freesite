"""
Copyright (c) Vitaliy Prikhodko
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of Vitaliy Prikhodko nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL VITALIY PRIKHODKO BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""


import os

from django.shortcuts import render, get_object_or_404, redirect

from freesite.settings import STATIC_ROOT
from .models import Page, MenuPage, Settings


STATIC_ROOT = STATIC_ROOT.replace("\\", "/")

favicon_exists = False
if os.path.isfile(os.path.join(STATIC_ROOT, 'favicon.png')):
    favicon_exists = True

logo_exists = False
if os.path.isfile(os.path.join(STATIC_ROOT, 'logo.png')):
    logo_exists = True

header_img_exists = False
if os.path.isfile(os.path.join(STATIC_ROOT, 'header.jpg')):
    header_img_exists = True

settings = Settings.objects.all()
menu_pages = MenuPage.objects.order_by('number')
pages = Page.objects.all()


def menu_page(request, pk):
    page = get_object_or_404(MenuPage, pk=pk)
    if page.title == settings[0].main_page_title:
        return redirect('main_page')
    if page.title == settings[0].page_list_title:
        return redirect('page_list', pk=pk)
    return render(request, 'page.html', {
        'menu_pages': menu_pages,
        'page': page,
        'settings': settings[0],
        'favicon_exists': favicon_exists,
        'logo_exists': logo_exists,
        'header_img_exists': header_img_exists,
        'STATIC_ROOT': STATIC_ROOT
    })


def page_list(request, pk):
    page = get_object_or_404(MenuPage, pk=pk)
    return render(request, 'page_list.html', {
        'menu_pages': menu_pages,
        'pages': pages,
        'page': page,
        'settings': settings[0],
        'favicon_exists': favicon_exists,
        'logo_exists': logo_exists,
        'header_img_exists': header_img_exists,
        'STATIC_ROOT': STATIC_ROOT
    })


def main_page(request):
    page = get_object_or_404(MenuPage, title=settings[0].main_page_title)
    return render(request, 'page.html', {
        'menu_pages': menu_pages,
        'page': page,
        'settings': settings[0],
        'favicon_exists': favicon_exists,
        'logo_exists': logo_exists,
        'header_img_exists': header_img_exists,
        'STATIC_ROOT': STATIC_ROOT
    })


def page(request, pk):
    page = get_object_or_404(Page, pk=pk)
    return render(request, 'page.html', {
        'menu_pages': menu_pages,
        'page': page,
        'settings': settings[0],
        'favicon_exists': favicon_exists,
        'logo_exists': logo_exists,
        'header_img_exists': header_img_exists,
        'STATIC_ROOT': STATIC_ROOT
    })


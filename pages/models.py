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


from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Page(models.Model):
    title = models.TextField()
    content = RichTextUploadingField()

    def __str__(self):
        return self.title


class MenuPage(models.Model):
    number = models.IntegerField()
    title = models.TextField()
    content = RichTextUploadingField()

    def __str__(self):
        return self.title


class Settings(models.Model):
    site_title = models.TextField(default="#")
    main_page_title = models.TextField(default="#")
    page_list_title = models.TextField(default="#")
    header_color = models.TextField(default="#")
    up_button_color = models.TextField(default="#")
    menu_color = models.TextField(default="#")
    menu_text_color = models.TextField(default="#")
    page_color = models.TextField(default="#")
    page_text_color = models.TextField(default="#")
    page_text_max_width = models.IntegerField(default=1024)

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
    site_title = models.TextField()
    header_color = models.TextField()
    menu_text_color = models.TextField()
    page_color = models.TextField()
    page_text_color = models.TextField()
    main_page_title = models.TextField()
    page_list_title = models.TextField()
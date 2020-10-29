from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Page(models.Model):
    number = models.IntegerField()
    title = models.TextField()
    content = RichTextUploadingField()

    def __str__(self):
        return self.title

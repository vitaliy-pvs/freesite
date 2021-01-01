# Generated by Django 3.1.4 on 2021-01-01 19:22

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('title', models.TextField()),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_title', models.TextField(default='#')),
                ('header_color', models.TextField(default='#')),
                ('up_burger_color', models.TextField(default='#')),
                ('menu_color', models.TextField(default='#')),
                ('menu_text_color', models.TextField(default='#')),
                ('page_color', models.TextField(default='#')),
                ('page_text_color', models.TextField(default='#')),
                ('main_page_title', models.TextField(default='#')),
                ('page_list_title', models.TextField(default='#')),
            ],
        ),
    ]

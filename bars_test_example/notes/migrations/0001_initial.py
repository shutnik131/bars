# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('head_line', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('body_text', models.TextField(verbose_name='Содержание')),
                ('favorite', models.BooleanField(verbose_name='Добавить в избранное', default=False)),
                ('categories', models.CharField(max_length=4, verbose_name='Категория', choices=[('link', 'Ссылка'), ('memo', 'Памятка'), ('note', 'Заметка'), ('todo', 'TODO')], default='note')),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('author', models.OneToOneField(to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'заметку',
                'verbose_name_plural': 'Заметки',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100, verbose_name='Тэг')),
            ],
            options={
                'verbose_name': 'тэг',
                'verbose_name_plural': 'Тэги',
            },
        ),
        migrations.AddField(
            model_name='note',
            name='tags',
            field=models.ManyToManyField(verbose_name='Тэги', to='notes.Tag'),
        ),
    ]

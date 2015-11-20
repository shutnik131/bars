# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('head_line', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('body_text', models.TextField()),
                ('favorite', models.BooleanField(default=False)),
                ('categories', models.CharField(max_length=4, choices=[('link', 'Ссылка'), ('memo', 'Памятка'), ('note', 'Заметка'), ('todo', 'TODO')], default='note')),
                ('pub_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Тэг')),
            ],
        ),
        migrations.AddField(
            model_name='note',
            name='tags',
            field=models.ManyToManyField(to='notes.Tag'),
        ),
    ]

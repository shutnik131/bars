from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Tag(models.Model):
    name = models.CharField('Тэг', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'тэг'
        verbose_name_plural = 'Тэги'


class Note(models.Model):
    category_list = (
        ('link', 'Ссылка'),
        ('memo', 'Памятка'),
        ('note', 'Заметка'),
        ('todo', 'TODO'),
    )
    head_line = models.CharField('Заголовок', max_length=100)
    body_text = models.TextField('Содержание')
    favorite = models.BooleanField('Добавить в избранное', default=False)
    tags = models.ManyToManyField(Tag, verbose_name='Тэги')
    categories = models.CharField('Категория', max_length=4, choices=category_list, default='note')
    pub_date = models.DateField(auto_now_add=True)
    author = models.OneToOneField(User, verbose_name='Автор')

    def __str__(self):
        return self.head_line

    class Meta:
        verbose_name = 'заметку'
        verbose_name_plural = 'Заметки'

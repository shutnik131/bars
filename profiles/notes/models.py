from django.db import models
from django.contrib.auth.models import User, UserManager

# Create your models here.


class Tag(models.Model):
    tagline = models.CharField(max_length=100)

    def __str__(self):
        return self.tagline


class Note(models.Model):
    header = models.CharField(max_length=100)
    body_text = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(User)

    def __str__(self):
        return self.header
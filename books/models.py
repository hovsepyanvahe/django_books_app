from django.db import models
from django.contrib.auth.models import User

from mptt.models import MPTTModel, TreeForeignKey


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Section(MPTTModel):
    title = models.CharField(max_length=255)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
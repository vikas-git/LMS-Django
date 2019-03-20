from django.db import models
from django.utils import timezone


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=128, blank=False, null=False, default=None)
    price = models.IntegerField(blank=True, null=True,)
    quantity = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:         
        db_table = 'books'


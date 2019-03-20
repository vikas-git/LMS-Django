from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=128, blank=True, null=True)
    role = models.IntegerField(blank=True, null=True, help_text='1->Student, 2->Faculty 3->Admin', choices=((1, 'Student'), (2, 'Faculty'), (3, 'Admin')))
    mobile = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email

    class Meta:         
        db_table = 'users'


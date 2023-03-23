from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class People(models.Model):
    first_name = models.CharField('First name', max_length=100)
    last_name = models.CharField('Last name', max_length=100)
    email = models.EmailField('Email')

    def __str__(self):
        return "%s %s %s" % (self.first_name, self.last_name, self.email)


class Log(models.Model):
    CHOICES = (
        ('CONNECT', 'CONNECT'),
        ('DELETE', 'DELETE'),
        ('GET', 'GET'),
        ('HEAD', 'HEAD'),
        ('OPTIONS', 'OPTIONS'),
        ('POST', 'POST'),
        ('PUT', 'PUT'),
    )
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=7, choices=CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    data = models.JSONField(null=True, blank=True)

    def __str__(self):
        return "%s %s %s %s %s" % (self.path, self.method, self.timestamp, self.user, self.data)

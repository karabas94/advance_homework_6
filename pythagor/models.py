from django.db import models


class People(models.Model):
    first_name = models.CharField('First name', max_length=100)
    last_name = models.CharField('Last name', max_length=100)
    email = models.EmailField('Email')

    def __str__(self):
        return "%s %s %s" % (self.first_name, self.last_name, self.email)

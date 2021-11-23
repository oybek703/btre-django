from django.db import models
from _datetime import datetime


class Contact(models.Model):
    listing = models.CharField(max_length=256)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name

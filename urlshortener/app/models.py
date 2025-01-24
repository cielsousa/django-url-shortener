from django.db import models

# Create your models here.

class Url (models.Model):
    date_shorten = models.DateField(auto_now=True)
    url_original = models.CharField(primary_key=True, max_length=256)
    url_shorted = models.CharField(max_length=256)
    number_visits = models.IntegerField()

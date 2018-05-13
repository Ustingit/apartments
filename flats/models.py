from django.db import models
import datetime
from django.utils import timezone


class Flat(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    flat_url = models.CharField(max_length=200)
    flat_id = models.IntegerField()
    price = models.CharField(max_length=50)
    phone_text = models.CharField(max_length=25)
    phone_img = models.ImageField()
    flat_name = models.CharField(max_length=200)
    owner = models.CharField(max_length=100)
    about = models.CharField(max_length=1000)

    def __str__(self):
        return "id: " + str(self.flat_id) + " title: " + str(self.title) + " .\n"

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

import datetime

from django.db import models
from django.utils import timezone

class note(models.Model):
    title_text = models.CharField(max_length=200)
    content_text = models.CharField(max_length=2000)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.title_text
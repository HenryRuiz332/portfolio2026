import os
from django.db import models
from config.timestamps import Timestamp

class Service(Timestamp):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='public/images/services/', null=True, blank=True)
    icon = models.CharField(max_length=100, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.title

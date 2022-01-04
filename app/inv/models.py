from django.db import models

from base.models import ModelClass
# Create your models here.

class Category(ModelClass):
    description = models.CharField(max_length=100, help_text='Category Description', unique=True)
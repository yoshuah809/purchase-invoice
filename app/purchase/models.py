from django.db import models

from bases.models import ModelClass

# Create your models here.

class Provider(ModelClass):
  name = models.CharField(max_length=100, unique=True)
  address = models.CharField(max_length=250, null=True, blank=True)
  contact = models.CharField(max_length=100)
  phone_number = models.CharField(max_length=15, null=True, blank=True)
  email = models.CharField(max_length=100, null=True, blank=True)

  def __str__(self):
    return '{}'.format(self.name)

  def save(self):
    self.name = self.name.upper()   
    self.address = self.address.upper()  
    super(Provider, self).save() 
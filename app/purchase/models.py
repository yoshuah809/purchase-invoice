from django.db import models

from bases.models import ModelClass
from inv.models import Product

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


class PurchaseHeader(ModelClass):
  purchase_date=models.DateField(null=True,blank=True)
  observation=models.TextField(blank=True,null=True)
  invoice_no=models.CharField(max_length=100)
  invoice_date=models.DateField()
  sub_total=models.FloatField(default=0)
  discount=models.FloatField(default=0)
  total=models.FloatField(default=0)

  provider=models.ForeignKey(Provider,on_delete=models.CASCADE)
  
  def __str__(self):
    return '{}'.format(self.observation)

  def save(self):
    self.observation = self.observation.upper()
    if self.sub_total == None  or self.discount == None:
      self.sub_total = 0
      self.discount = 0
          
    self.total = self.sub_total - self.discount
    super(PurchaseHeader,self).save()

  class Meta:
    verbose_name="Purchase Header"    


class PurchaseDetail(ModelClass):
    purchase=models.ForeignKey(PurchaseHeader,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.BigIntegerField(default=0)
    provider_price=models.FloatField(default=0)
    sub_total=models.FloatField(default=0)
    discount=models.FloatField(default=0)
    total=models.FloatField(default=0)
    cost=models.FloatField(default=0)

    def __str__(self):
      return '{}'.format(self.product)

    def save(self):
      self.sub_total = float(float(int(self.quantity)) * float(self.provider_price))
      self.total = self.sub_total - float(self.discount)
      super(PurchaseDetail, self).save()
    
    class Meta:
      verbose_name="Purchase Detail"
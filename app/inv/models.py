from django.db import models

from bases.models import ModelClass
# Create your models here.

class Category(ModelClass):
    description = models.CharField(max_length=100, help_text='Category Description', unique=True)

    def __str__(self):
        return '{}'.format(self.description)

    def save(self):
        self.description = self.description.upper()    
        super(Category, self).save()


class SubCategory(ModelClass):
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, help_text='Category Description')

    def __str__(self):
       return '{}:{}'.format(self.category.description, self.description)

    def save(self):
        self.description = self.description.upper()    
        super(SubCategory, self).save()   

    class Meta:
        unique_together = ('category', 'description')


class Brand(ModelClass):
    description =models.CharField(max_length=100, help_text='Brand Description', unique = True)

    def __str__(self):
       return '{}'.format(self.description)

    def save(self):
       self.description = self.description.upper()    
       super(Brand, self).save()   


class Unit(ModelClass):
    description =models.CharField(max_length=100, help_text='Unit Description', unique = True)

    def __str__(self):
       return '{}'.format(self.description)

    def save(self):
       self.description = self.description.upper()    
       super(Unit, self).save()  


class Product(ModelClass):
    code =models.CharField(max_length=20, unique = True)       
    bar_code = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    in_stock = models.IntegerField(default=0)
    last_purchased = models.DateField(null=True, blank=True)
    
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    def __str__(self):
      return '{}'.format(self.description)

    def save(self):
      self.description = self.description.upper()    
      super(Product, self).save()    

    class Meta:
       unique_together = ('code', 'bar_code')  
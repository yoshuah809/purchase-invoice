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
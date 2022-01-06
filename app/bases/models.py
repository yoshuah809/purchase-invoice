from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class ModelClass(models.Model):
    is_active = models.BooleanField(default=True, blank=True, null=True )
    date_created = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    modified_by = models.IntegerField(blank = True, null = True)

    class Meta:
        abstract=True

        



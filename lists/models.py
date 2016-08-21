from django.db import models
#from django.template.defaultfilters import default
class Item(models.Model):
    text=models.TextField(default='')
# Create your models here.

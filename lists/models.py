from django.db import models
#from django.template.defaultfilters import default
class List(models.Model):
    pass
class Item(models.Model):
    text=models.TextField(default='')
    list=models.ForeignKey(List,default=None)
# Create your models here.

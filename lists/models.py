from django.db import models

# Create your models here.
class Item(models.Model):
    text = models.CharField(max_length=100)
    list = models.ForeignKey(to='List', default=None)
    

class List(models.Model):
    pass
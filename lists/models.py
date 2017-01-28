from django.db import models

# Create your models here.
class Item(models.Model):
    text = models.TextField(max_length=100, default='', blank=False)
    list = models.ForeignKey(to='List', default=None)
    

class List(models.Model):
    pass
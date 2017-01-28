from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Item(models.Model):
    text = models.TextField(max_length=100, default='', blank=False)
    list = models.ForeignKey(to='List', default=None)
    

class List(models.Model):
    pass

    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])
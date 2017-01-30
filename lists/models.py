from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Item(models.Model):
    text = models.TextField(max_length=200, default='', blank=False)
    list = models.ForeignKey(to='List', default=None)
    
    def __str__(self):
        return self.text
    
    class Meta:
        unique_together = ('list', 'text')

class List(models.Model):
    pass

    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])
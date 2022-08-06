from django.db import models
from django.urls import reverse

class Drum(models.Model):
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('drums_detail', kwargs={'drum_id': self.id})
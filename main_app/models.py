from django.db import models
from django.urls import reverse
from datetime import date

ACTIONS = (
  ('T', 'Tuning'),
  ('R', 'Re-heading'),
  ('C', 'Cleaning')
)

class Accessory(models.Model):
  name = models.CharField(max_length=50)
  use = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('accessories_detail', kwargs={'pk': self.id})

class Drum(models.Model):
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('drums_detail', kwargs={'drum_id': self.id})
  
  def maintenanced_today(self):
    return self.maintenance_set.filter(date=date.today()).count() >= len(ACTIONS)

class Maintenance(models.Model):
  date = models.DateField('Maintenance date')
  action = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=ACTIONS,
    # set the default value for action to be 'T'
    default=ACTIONS[0][0]
  )

  # Create a drum_id column in the database
  drum = models.ForeignKey(Drum, on_delete=models.CASCADE)

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_action_display()} on {self.date}"

    class Meta:
      ordering = ['-date']

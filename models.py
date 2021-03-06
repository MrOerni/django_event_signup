from django.contrib.auth.models import User
from django.db import models


class Event(models.Model):
    name = models.CharField(blank=False, max_length=64)
    date = models.DateField(blank=False)
    location = models.TextField(blank=True)
    description = models.TextField(blank=True)

    class Meta:
        get_latest_by = 'date'

    def __str__(self):
        display = "{0} am {1}"
        return display.format(self.name, self.date)


class Participant(models.Model):
    user = models.ForeignKey(User)
    event = models.ForeignKey(Event)

    class Meta:
        unique_together = ('user', 'event')

    def __str__(self):
        display = "Teilnahme von {0} an {1}"
        return display.format(self.user, self.event)

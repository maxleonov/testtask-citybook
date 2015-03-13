from django.db import models

class City(models.Model):

    class Meta:
        verbose_name_plural = 'Cities'

    name = models.CharField(u'Name', max_length=255, unique=True, blank=False, primary_key=True)
    food = models.CharField(u'Food', max_length=255)
    timezone = models.CharField(u'Time Zone', max_length=6)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


from  django.db import models


class SakaiGarage(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField()
    phone = models.IntegerField(default=1)
    logbook = models.CharField(max_length=40, blank=False)
    make = models.CharField(max_length=9, blank=False)
    model = models.CharField(max_length=30)
    chasis = models.CharField(max_length=30, blank=False, null=False)
    damages = models.CharField(max_length=30, blank=False, null=False)
    insuarance = models.CharField(max_length=30, blank=False, null=False)

def __str__(self):
    return self.name















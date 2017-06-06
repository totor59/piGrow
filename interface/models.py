# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

##################################################
#                                                #
#             AMBIENT TEMPERATURE                #
#                                                #
##################################################

class Temperature(models.Model):
    temp = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Température")
    date = date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de relevé")

    def __str__(self):
        return format(self.temp)

##################################################
#                                                #
#             HYGROMETRY                         #
#                                                #
##################################################

class Hygrometry(models.Model):
    hygro = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Hygrométrie")
    date = date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de relevé")
    
    def __str__(self):
        return format(self.hygro)

##################################################
#                                                #
#             SOIL MOISTURE                      #
#                                                #
##################################################

class Soil_moisture(models.Model):
    moisture = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Humidité du sol")
    date = date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de relevé")

    def __str__(self):
        return format(self.moisture)


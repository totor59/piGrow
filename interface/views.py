# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from datetime import datetime
from interface.models import Temperature, Hygrometry, Soil_moisture
# Create your views here.
def hub(request):
    temp = Temperature.objects.latest('temp')
    date = datetime.now()
    return render(request, 'interface/hub.html', locals())





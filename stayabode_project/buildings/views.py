# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse

from .models import Resident

# Create your views here.


def get_residents(request):
    building_id = request.GET.get('id')
    residents = Resident.objects.filter(building_id=building_id).all()
    residents_list = list()
    for resident in residents:
        residents_list.append({'id': resident.id, 'title': '{0} {1}'.format(resident.first_name, resident.last_name)})
    return JsonResponse({'res': residents_list})

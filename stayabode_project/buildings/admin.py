# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Building, Resident, Event
from .forms import EventForm

# Register your models here.


class ResidentInline(admin.StackedInline):
    model = Resident
    extra = 1


class BuildingAdmin(admin.ModelAdmin):
    inlines = [
        ResidentInline,
    ]
    list_display = ('building_name', 'building_location')

    search_fields = ['building_name', 'building_location']
    list_filter = ('building_name', 'building_location')


class ResidentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'building_name')
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ('first_name', 'last_name', 'email')

    def building_name(self, obj):
        return obj.building.building_name

    building_name.short_description = 'Building'
    building_name.admin_order_field = 'building__building_name'


class EventAdmin(admin.ModelAdmin):

    class Media:
        js = ('/static/buildings/admin/buildings.js',)

    form = EventForm

    list_display = ('event_title', 'event_description', 'event_date')

    search_fields = ['event_title', 'event_description', 'event_date']
    list_filter = ('event_title', 'event_description', 'event_date')


admin.site.register(Building, BuildingAdmin)
admin.site.register(Resident, ResidentAdmin)
admin.site.register(Event, EventAdmin)

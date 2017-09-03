# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.


class Building(models.Model):

    building_name = models.CharField(max_length=255)
    building_location = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.building_name


class Resident(models.Model):
    building = models.ForeignKey(Building)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Event(models.Model):

    event_title = models.CharField(max_length=255)
    event_description = models.CharField(max_length=255)
    event_date = models.DateTimeField()

    buildings = models.ManyToManyField(Building)
    residents = models.ManyToManyField(Resident)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event_title

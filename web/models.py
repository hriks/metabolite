# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import csv
import uuid


class Intensity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    value = models.FloatField(default=0.0)
    created = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create_entries(cls, *args, **kwargs):
        return cls.objects.create(*args, **kwargs)

    @staticmethod
    def read_csv(filename, delimiter=','):
        with open(filename, 'rb') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=delimiter)
            for row in reader:
                tmp = {
                    'label': row.get('Label'),
                    'value': row.get('NA Corrected with zero'),
                    'name': row.get('Name')
                }
                Intensity.create_entries(**tmp)

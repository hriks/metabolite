# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import uuid


class Intensity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    value = models.FloatField(default=0.0)
    created = models.DateTimeField(auto_now_add=True)

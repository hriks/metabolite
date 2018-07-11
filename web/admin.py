# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from web.models import Intensity


@admin.register(Intensity)
class IntensityAdmin(admin.ModelAdmin):
    list_display = ("name", "value", "label", "created")
    search_fields = ("label",)

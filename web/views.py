from __future__ import unicode_literals

from django.utils.decorators import method_decorator
from django.shortcuts import render
from django import views
from django.http import JsonResponse
from django.db.models import Sum

from web.models import Intensity


class Dashboard(views.View):
    template_name = 'dashboard.html'
    metabolites = [name[0] for name in Intensity.objects.all().values_list('name').distinct()]

    @method_decorator(views.decorators.csrf.csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Dashboard, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(
            request, self.template_name, {'metabolites': self.metabolites})


class MetaboliteInformations(views.View):
    template_name = 'dashboard.html'

    @method_decorator(views.decorators.csrf.csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(
            MetaboliteInformations, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return JsonResponse(
            {'response': self.get_data(request.GET.get('query'))}, status=200
        )

    def get_data(self, metabolite):
        intensity = Intensity.objects.filter(name=metabolite)
        labels = [label[0] for label in intensity.values_list('label').distinct()] # noqa
        values = dict.fromkeys(labels, 0)
        for label in labels:
            distinct_intensity = intensity.filter(label=label)
            values[label] = round((distinct_intensity.aggregate(
                s=Sum('value'))['s'] or 0) / distinct_intensity.count(), 2)
        return values

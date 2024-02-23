from django.shortcuts import render
from django.views.generic import TemplateView


class IbanistView(TemplateView):
    template_name = 'index.html'

class BanksView(TemplateView):
    template_name = 'banks.html'


# Create your views here.

from django.shortcuts import render
from django.views.generic import TemplateView


class TemplateCall(TemplateView):
    template_name = 'base.html'


# Create your views here.

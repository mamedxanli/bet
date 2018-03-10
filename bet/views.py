from django.views import generic
from django.shortcuts import render



class HomePage(generic.TemplateView):
    template_name = "bet/index.html"


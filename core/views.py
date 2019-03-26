from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, TemplateView, CreateView, UpdateView, FormView, ListView


# Create your views here.
class IndexView(TemplateView):
	template_name = 'index.html'

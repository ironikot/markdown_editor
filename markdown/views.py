from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from .models import Article

# Create your views here.


class HomePageView(CreateView):
    model = Article
    template_name = 'home.html'
    fields = [ 'content']


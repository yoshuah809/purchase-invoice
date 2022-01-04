from django.shortcuts import render
from django.views import generic
from .models import Category

from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class CategoryView(LoginRequiredMixin, generic.ListView):
    model = Category
    template_name = "inv/category_list.html"
    context_object_name= "obj"
    login_url='bases:login'

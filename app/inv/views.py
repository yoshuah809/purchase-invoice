from django.shortcuts import render
from django.views import generic
from .models import Category
from .forms import CategoryForm
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class CategoryView(LoginRequiredMixin, generic.ListView):
    model = Category
    template_name = "inv/category_list.html"
    context_object_name= "obj"
    login_url='bases:login'


class NewCategory(LoginRequiredMixin, generic.CreateView):
    model=Category
    template_name = 'inv/category_form.html'
    context_object_name='obj'
    form_class=CategoryForm
    success_url=reverse_lazy("inv:category_list")
    login_url='bases:login'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class EditCategory(LoginRequiredMixin, generic.UpdateView):
    model=Category
    template_name = 'inv/category_form.html'
    context_object_name='obj'
    form_class=CategoryForm
    success_url=reverse_lazy("inv:category_list")
    login_url='bases:login'

    def form_valid(self, form):
        form.instance.modified_by = self.request.user.id
        return super().form_valid(form)
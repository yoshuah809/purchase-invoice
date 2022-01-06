from django.shortcuts import render
from django.views import generic
from .models import Category, SubCategory
from .forms import CategoryForm, SubCategoryForm
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

class DeleteCategory(LoginRequiredMixin, generic.DeleteView):
    model=Category
    template_name = 'inv/delete_category.html'
    context_object_name='obj'
    success_url=reverse_lazy("inv:category_list")


class SubCategoryView(LoginRequiredMixin, generic.ListView):
    model = SubCategory
    template_name = "inv/subcategory_list.html"
    context_object_name= "obj"
    login_url='bases:login'


class NewSubCategory(LoginRequiredMixin, generic.CreateView):
    model=SubCategory
    template_name = 'inv/subcategory_form.html'
    context_object_name='obj'
    form_class=SubCategoryForm
    success_url=reverse_lazy("inv:subcategory_list")
    login_url='bases:login'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)    
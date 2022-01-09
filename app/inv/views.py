from django.shortcuts import render, redirect
from django.views import generic
from .models import Brand, Category, Product, SubCategory, Unit
from .forms import BrandForm, CategoryForm, ProductForm, SubCategoryForm, UnitForm
from django.urls import reverse_lazy
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

class CategoryView(LoginRequiredMixin, PermissionRequiredMixin,generic.ListView):
    permission_required='inv.view_category'
    model = Category
    template_name = "inv/category_list.html"
    context_object_name= "obj"
    login_url='bases:login'


class NewCategory(SuccessMessageMixin, LoginRequiredMixin, generic.CreateView):
    model=Category
    template_name = 'inv/category_form.html'
    context_object_name='obj'
    form_class=CategoryForm
    success_url=reverse_lazy("inv:category_list")
    login_url='bases:login'
    success_message='The Category was successfully created'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class EditCategory(SuccessMessageMixin,LoginRequiredMixin, generic.UpdateView):
    model=Category
    template_name = 'inv/category_form.html'
    context_object_name='obj'
    form_class=CategoryForm
    success_url=reverse_lazy("inv:category_list")
    login_url='bases:login'
    success_message="The Category was successfully updated"

    def form_valid(self, form):
        form.instance.modified_by = self.request.user.id
        return super().form_valid(form)

class DeleteCategory(LoginRequiredMixin, generic.DeleteView):
    model=Category
    template_name = 'inv/delete_category.html'
    context_object_name='obj'
    success_url=reverse_lazy("inv:category_list")


class SubCategoryView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required='inv.view_subcategory'
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



class EditSubCategory(LoginRequiredMixin, generic.UpdateView):
    model=SubCategory
    template_name = 'inv/subcategory_form.html'
    context_object_name='obj'
    form_class=SubCategoryForm
    success_url=reverse_lazy("inv:subcategory_list")
    login_url='bases:login'

    def form_valid(self, form):
        form.instance.modified_by = self.request.user.id
        return super().form_valid(form)


class DeleteSubCategory(LoginRequiredMixin, generic.DeleteView):
    model=SubCategory
    template_name = 'inv/delete_category.html'
    context_object_name='obj'
    success_url=reverse_lazy("inv:subcategory_list")



class BrandView(LoginRequiredMixin, generic.ListView):
    model = Brand
    template_name = "inv/brand_list.html"
    context_object_name= "obj"
    login_url='bases:login'    

class NewBrand(LoginRequiredMixin, generic.CreateView):
    model=Brand
    template_name = 'inv/brand_form.html'
    context_object_name='obj'
    form_class=BrandForm
    success_url=reverse_lazy("inv:brand_list")
    login_url='bases:login'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class EditBrand(LoginRequiredMixin, generic.UpdateView):
    model=Brand
    template_name = 'inv/brand_form.html'
    context_object_name='obj'
    form_class=BrandForm
    success_url=reverse_lazy("inv:brand_list")
    login_url='bases:login'

    def form_valid(self, form):
        form.instance.modified_by = self.request.user.id
        return super().form_valid(form)    


def deactivate_brand(request, id):
    brand = Brand.objects.filter(pk=id).first()
    context={}
    template_name='inv/delete_catalog.html'

    if not brand:
        return redirect('inv:brand_list')

    if request.method == 'GET':
        context = {'obj': brand }

    if request.method == 'POST':
        brand.is_active = False
        brand.save()
        messages.success(request, 'Brand has been deactivated')
        return redirect("inv:brand_list")    

    return render(request, template_name, context)    


class UnitView(LoginRequiredMixin, generic.ListView):
    model = Unit
    template_name = "inv/unit_list.html"
    context_object_name= "obj"
    login_url='bases:login' 


class NewUnit(LoginRequiredMixin, generic.CreateView):
    model=Unit
    template_name = 'inv/unit_form.html'
    context_object_name='obj'
    form_class=UnitForm
    success_url=reverse_lazy("inv:unit_list")
    login_url='bases:login'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class EditUnit(LoginRequiredMixin, generic.UpdateView):
    model=Unit
    template_name = 'inv/unit_form.html'
    context_object_name='obj'
    form_class=UnitForm
    success_url=reverse_lazy("inv:unit_list")
    login_url='bases:login'

    def form_valid(self, form):
        form.instance.modified_by = self.request.user.id
        return super().form_valid(form)   


def deactivate_unit(request, id):
    unit = Unit.objects.filter(pk=id).first()
    context={}
    template_name='inv/delete_catalog.html'

    if not unit:
        return redirect('inv:unit_list')

    if request.method == 'GET':
        context = {'obj': unit }

    if request.method == 'POST':
        unit.is_active = False
        unit.save()
        return redirect("inv:unit_list")    

    return render(request, template_name, context) 


class ProductsView(LoginRequiredMixin, generic.ListView):
    model = Product
    template_name = "inv/product_list.html"
    context_object_name= "obj"
    login_url='bases:login' 


class NewProduct(LoginRequiredMixin, generic.CreateView):
    model=Product
    template_name = 'inv/product_form.html'
    context_object_name='obj'
    form_class=ProductForm
    success_url=reverse_lazy("inv:product_list")
    login_url='bases:login'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)    


class EditProduct(LoginRequiredMixin, generic.UpdateView):
    model=Product
    template_name = 'inv/product_form.html'
    context_object_name='obj'
    form_class=ProductForm
    success_url=reverse_lazy("inv:product_list")
    login_url='bases:login'

    def form_valid(self, form):
        form.instance.modified_by = self.request.user.id
        return super().form_valid(form)  


def deactivate_product(request, id):
    product = Product.objects.filter(pk=id).first()
    context={}
    template_name='inv/delete_catalog.html'

    if not product:
        return redirect('inv:product_list')

    if request.method == 'GET':
        context = {'obj': product }

    if request.method == 'POST':
        product.is_active = False
        product.save()
        return redirect("inv:product_list")    

    return render(request, template_name, context)         
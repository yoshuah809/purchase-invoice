from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import generic
from .models import Brand, Category, Product, SubCategory, Unit
from .forms import BrandForm, CategoryForm, ProductForm, SubCategoryForm, UnitForm
from django.urls import reverse_lazy
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from bases.views import NoProvileges

from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

class CategoryView(LoginRequiredMixin, PermissionRequiredMixin,generic.ListView):
    permission_required='inv.view_category'
    model = Category
    template_name = "inv/category_list.html"
    context_object_name= "obj"
    login_url='bases:login'


class NewCategory(SuccessMessageMixin, NoProvileges, generic.CreateView):
    permission_required='inv.new_category'
    model=Category
    template_name = 'inv/category_form.html'
    context_object_name='obj'
    form_class=CategoryForm
    success_url=reverse_lazy("inv:category_list")
    success_message='The Category was successfully created'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class EditCategory(SuccessMessageMixin, NoProvileges, generic.UpdateView):
    permission_required='inv.edit_category'
    model=Category
    template_name = 'inv/category_form.html'
    context_object_name='obj'
    form_class=CategoryForm
    success_url=reverse_lazy("inv:category_list")
    success_message="The Category was successfully updated"

    def form_valid(self, form):
        form.instance.modified_by = self.request.user.id
        return super().form_valid(form)

class DeleteCategory(NoProvileges, generic.DeleteView):
    permission_required='inv.delete_category'
    model=Category
    template_name = 'inv/delete_category.html'
    context_object_name='obj'
    success_url=reverse_lazy("inv:category_list")


class SubCategoryView(NoProvileges, generic.ListView):
    permission_required='inv.view_subcategory'
    model = SubCategory
    template_name = "inv/subcategory_list.html"
    context_object_name= "obj"
    


class NewSubCategory(NoProvileges, generic.CreateView):
    permission_required='inv.new_subcategory'
    model=SubCategory
    template_name = 'inv/subcategory_form.html'
    context_object_name='obj'
    form_class=SubCategoryForm
    success_url=reverse_lazy("inv:subcategory_list")
    

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)    



class EditSubCategory(NoProvileges, generic.UpdateView):
    permission_required='inv.edit_subcategory'
    model=SubCategory
    template_name = 'inv/subcategory_form.html'
    context_object_name='obj'
    form_class=SubCategoryForm
    success_url=reverse_lazy("inv:subcategory_list")
    

    def form_valid(self, form):
        form.instance.modified_by = self.request.user.id
        return super().form_valid(form)


class DeleteSubCategory(NoProvileges, generic.DeleteView):
    permission_required='inv.delete_subcategory'
    model=SubCategory
    template_name = 'inv/delete_category.html'
    context_object_name='obj'
    success_url=reverse_lazy("inv:subcategory_list")



class BrandView(NoProvileges, generic.ListView):
    permission_required='inv.view_brand'
    model = Brand
    template_name = "inv/brand_list.html"
    context_object_name= "obj"
      

class NewBrand(NoProvileges, generic.CreateView):
    permission_required='inv.new_brand'
    model=Brand
    template_name = 'inv/brand_form.html'
    context_object_name='obj'
    form_class=BrandForm
    success_url=reverse_lazy("inv:brand_list")
    

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class EditBrand(NoProvileges, generic.UpdateView):
    permission_required='inv.edit_brand'
    model=Brand
    template_name = 'inv/brand_form.html'
    context_object_name='obj'
    form_class=BrandForm
    success_url=reverse_lazy("inv:brand_list")
   
    def form_valid(self, form):
        form.instance.modified_by = self.request.user.id
        return super().form_valid(form)    

@login_required(login_url='/login/')
@permission_required('inv.change_brand', login_url='bases:no_privileges')
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


class UnitView(NoProvileges, generic.ListView):
    permission_required='inv.view_unit'
    model = Unit
    template_name = "inv/unit_list.html"
    context_object_name= "obj"
    

class NewUnit(NoProvileges, generic.CreateView):
    permission_required='inv.new_unit'
    model=Unit
    template_name = 'inv/unit_form.html'
    context_object_name='obj'
    form_class=UnitForm
    success_url=reverse_lazy("inv:unit_list")
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class EditUnit(NoProvileges, generic.UpdateView):
    permission_required='inv.unit_list'
    model=Unit
    template_name = 'inv/unit_form.html'
    context_object_name='obj'
    form_class=UnitForm
    success_url=reverse_lazy("inv:unit_list")
  
    def form_valid(self, form):
        form.instance.modified_by = self.request.user.id
        return super().form_valid(form)   

@login_required(login_url='/login/')
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


class ProductsView(NoProvileges, generic.ListView):
    permission_required='inv.view_product'
    model = Product
    template_name = "inv/product_list.html"
    context_object_name= "obj"
    


class NewProduct(NoProvileges, generic.CreateView):
    permission_required='inv.new_product'
    model=Product
    template_name = 'inv/product_form.html'
    context_object_name='obj'
    form_class=ProductForm
    success_url=reverse_lazy("inv:product_list")
    

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)    


class EditProduct(NoProvileges, generic.UpdateView):
    permission_required='inv.edit_product'
    model=Product
    template_name = 'inv/product_form.html'
    context_object_name='obj'
    form_class=ProductForm
    success_url=reverse_lazy("inv:product_list")
    
    def form_valid(self, form):
        form.instance.modified_by = self.request.user.id
        return super().form_valid(form)  

@login_required(login_url='/login/')
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
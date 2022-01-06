from django.urls import path

from .views import BrandView, CategoryView, DeleteSubCategory, EditCategory, EditSubCategory, NewBrand, NewCategory, DeleteCategory, NewSubCategory, SubCategoryView, EditBrand

urlpatterns = [

    path('categories/', CategoryView.as_view(), name='category_list'),
    path('categories/new', NewCategory.as_view(), name='new_category'),
    path('categories/edit/<int:pk>', EditCategory.as_view(), name='edit_category'),
    path('categories/delete/<int:pk>', DeleteCategory.as_view(), name='delete_category'),
    
    path('subcategories/', SubCategoryView.as_view(), name='subcategory_list'),
    path('subcategories/new', NewSubCategory.as_view(), name='new_subcategory'),
    path('subcategories/edit/<int:pk>', EditSubCategory.as_view(), name='edit_subcategory'),
    path('subcategories/delete/<int:pk>', DeleteSubCategory.as_view(), name='delete_subcategory'),

    path('brands/', BrandView.as_view(), name='brand_list'),
    path('brands/new', NewBrand.as_view(), name='new_brand'),
    path('brands/edit/<int:pk>', EditBrand.as_view(), name='edit_brand'),


]
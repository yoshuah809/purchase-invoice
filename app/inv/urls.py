from django.urls import path

from .views import CategoryView, EditCategory, NewCategory, DeleteCategory, NewSubCategory, SubCategoryView

urlpatterns = [

    path('categories/', CategoryView.as_view(), name='category_list'),
    path('categories/new', NewCategory.as_view(), name='new_category'),
    path('categories/edit/<int:pk>', EditCategory.as_view(), name='edit_category'),
    path('categories/delete/<int:pk>', DeleteCategory.as_view(), name='delete_category'),
    
    path('subcategories/', SubCategoryView.as_view(), name='subcategory_list'),
    path('subcategories/new', NewSubCategory.as_view(), name='new_subcategory'),

]
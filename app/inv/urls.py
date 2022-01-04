from django.urls import path

from .views import CategoryView, EditCategory, NewCategory

urlpatterns = [

    path('categories/', CategoryView.as_view(), name='category_list'),
    path('categories/new', NewCategory.as_view(), name='new_category'),
    path('categories/edit/<int:pk>', EditCategory.as_view(), name='edit_category'),
]
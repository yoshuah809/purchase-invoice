from django.urls import path

from .views import EditProvider, NewProvider, ProviderView, deactivate_provider

urlpatterns = [

    path('providers/', ProviderView.as_view(), name='provider_list'),
    path('providers/new', NewProvider.as_view(), name='new_provider'),
    path('providers/edit/<int:pk>', EditProvider.as_view(), name='edit_provider'),
        
    path('providers/deactivate/<int:id>', deactivate_provider, name='deactivate_provider'),
  

]
from django.urls import path

from .views import EditProvider, NewProvider, ProviderView, PurchaseView, deactivate_provider, purchase

urlpatterns = [

    path('providers/', ProviderView.as_view(), name='provider_list'),
    path('providers/new', NewProvider.as_view(), name='new_provider'),
    path('providers/edit/<int:pk>', EditProvider.as_view(), name='edit_provider'),
        
    path('providers/deactivate/<int:id>', deactivate_provider, name='deactivate_provider'),
  
    path('purchase/', PurchaseView.as_view(), name='purchase_list'),
    path('purchase/new', purchase, name='new_purchase'),
    path('purchase/edit/<int:purchase_id>', purchase, name='edit_purchase'),
]
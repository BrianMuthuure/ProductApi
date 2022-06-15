from django.urls import path
from .views import ProductListCreateApiView, ProductDetailApiView,\
    ProductUpdateApiView, ProductDeleteApiView, ProductMixinView

urlpatterns = [
    path('', ProductListCreateApiView.as_view(), name='product_create_api_view'),
    path('<int:pk>/', ProductDetailApiView.as_view(), name='product_detail_api_view'),
    path('<int:pk>/update/', ProductUpdateApiView.as_view(), name='product_update_api_view'),
    path('<int:pk>/delete/', ProductDeleteApiView.as_view(), name='product_delete_api_view'),
]

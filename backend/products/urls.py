from django.urls import path

from backend.products.views.products_crud import ProductRetrieveAPIView

app_name = 'products'


urlpatterns = [
    path(
        '<int:product_pk>',
        ProductRetrieveAPIView.as_view(),
        name='retrieve_product',
    ),
]

from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response

from backend.products.models.products import Products
from backend.products.serializers.products_serializers import ProductsOutputSerializer


class ProductRetrieveAPIView(GenericAPIView):
    serializer_class = ProductsOutputSerializer
    lookup_url_kwarg = 'product_pk'

    def get(self, request: Request, product_pk: int):
        product = get_object_or_404(Products, pk=product_pk)
        self.check_object_permissions(request, product)
        return Response(data=self.get_serializer(product).data)

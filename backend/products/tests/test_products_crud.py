import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_retrieve_product(client, product):
    response = client.get(reverse('products:retrieve_product', kwargs={'product_pk': product.pk}))
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_retrieve_not_exist_product(client):
    response = client.get(reverse('products:retrieve_product', kwargs={'product_pk': 1}))
    assert response.status_code == status.HTTP_404_NOT_FOUND

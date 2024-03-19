import pytest

from backend.products.tests.factories import ProductBrandFactory


@pytest.fixture
def product():
    return ProductBrandFactory()

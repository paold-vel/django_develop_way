import factory.fuzzy

from backend.products.models.products import Products


class ProductBrandFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('word')
    is_active = True

    class Meta:
        model = Products

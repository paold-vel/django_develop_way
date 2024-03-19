from rest_framework import serializers


class ProductsOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50, required=True, allow_null=False, allow_blank=False, label='Название')
    is_active = serializers.BooleanField(required=True, allow_null=False, label='Активный')

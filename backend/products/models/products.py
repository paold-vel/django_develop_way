from django.db import models


class Products(models.Model):
    name = models.CharField(verbose_name='Название', max_length=50, blank=False, null=False)
    is_active = models.BooleanField(verbose_name='Активный', default=False)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        db_table = 'products'

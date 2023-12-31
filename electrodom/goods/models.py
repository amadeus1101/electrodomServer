from django.db import models


# class DBMixin(models.Model):
#     # using = 'default'  # По умолчанию, используем default базу данных
#
#     class Meta:
#         abstract = True
#
#     def save(self, *args, **kwargs):
#         using_db = getattr(self, 'using', self.using)
#         super().save(using=using_db, *args, **kwargs)


class Providers(models.Model):
    provider_name = models.CharField(max_length=255, verbose_name='Имя поставщика')

    class Meta:
        verbose_name = 'поставщика'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return f'{self.provider_name}'


class Categories(models.Model):
    category_name = models.CharField(max_length=255, verbose_name='Категория')

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.category_name}'


class Characteristic(models.Model):
    name = models.CharField(max_length=50, verbose_name='Характеристика')

    class Meta:
        verbose_name = 'характеристику'
        verbose_name_plural = 'Характеристики'

    def __str__(self):
        return f'{self.name}'


class Goods(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название товара')
    provider_id = models.ForeignKey(to=Providers, on_delete=models.CASCADE, null=True, verbose_name='Поставщик')
    category_id = models.ForeignKey(to=Categories, on_delete=models.CASCADE, null=True, verbose_name='Категория')
    price = models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Цена')
    count = models.PositiveIntegerField(verbose_name='Количество')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.name}'


class GoodsCharacteristic(models.Model):
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name='Товар')
    characteristic = models.ForeignKey(Characteristic, on_delete=models.CASCADE, verbose_name='Характеристика')
    value = models.CharField(max_length=50, verbose_name='Значение характеристики')

    class Meta:
        verbose_name = 'характеристика'
        verbose_name_plural = 'Характеристики'

    def __str__(self):
        return f'{self.characteristic}'


class Photo(models.Model):
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name='Товар')
    path = models.ImageField(upload_to='photo', verbose_name='Фотография')
    for_card = models.BooleanField()




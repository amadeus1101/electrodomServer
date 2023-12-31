# Generated by Django 4.2.3 on 2023-08-15 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_characteristic_goods_image_goodscharacteristic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goods',
            options={'verbose_name': 'товар', 'verbose_name_plural': 'Товаров'},
        ),
        migrations.AlterField(
            model_name='goods',
            name='category_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.categories', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='count',
            field=models.PositiveIntegerField(verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='image',
            field=models.ImageField(upload_to='product_images', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название товара'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='provider_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.providers', verbose_name='Поставщик'),
        ),
        migrations.AlterField(
            model_name='goodscharacteristic',
            name='characteristic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.characteristic', verbose_name='Характеристика'),
        ),
        migrations.AlterField(
            model_name='goodscharacteristic',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.goods', verbose_name='Товар'),
        ),
        migrations.AlterField(
            model_name='goodscharacteristic',
            name='value',
            field=models.CharField(max_length=50, verbose_name='Значение характеристики'),
        ),
    ]

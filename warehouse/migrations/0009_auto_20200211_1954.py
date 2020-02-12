# Generated by Django 3.0.3 on 2020-02-11 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0008_auto_20200203_2328'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cargo',
            options={'verbose_name': 'Поставка', 'verbose_name_plural': 'Поставки'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Покупатель', 'verbose_name_plural': 'Покупатели'},
        ),
        migrations.AlterModelOptions(
            name='shipment',
            options={'verbose_name': 'Покупка', 'verbose_name_plural': 'Покупки'},
        ),
        migrations.AlterModelOptions(
            name='stock',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='supplier',
            options={'verbose_name': 'Поставщик', 'verbose_name_plural': 'Поставщики'},
        ),
        migrations.AlterModelOptions(
            name='suppliercategory',
            options={'verbose_name': 'supplier_category', 'verbose_name_plural': 'supplier_categories'},
        ),
        migrations.AlterField(
            model_name='cargo',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата поставки'),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='status',
            field=models.CharField(choices=[('Исполнено', 'Исполнено'), ('В пути', 'В пути')], max_length=9, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='stocks',
            field=models.ManyToManyField(through='warehouse.CargoStock', to='warehouse.Stock', verbose_name='Товары'),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.Supplier', verbose_name='Поставщик'),
        ),
        migrations.AlterField(
            model_name='cargostock',
            name='number',
            field=models.IntegerField(verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='contact_info',
            field=models.TextField(null=True, verbose_name='Контактные данные'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='full_name',
            field=models.CharField(max_length=80, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=20, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.Customer', verbose_name='Покупатель'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата покупки'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='qr',
            field=models.TextField(null=True, verbose_name='Код подтверждения'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='status',
            field=models.CharField(choices=[('Исполнено', 'Исполнено'), ('Проверка', 'Проверка'), ('Собрано', 'Собрано'), ('Отменено', 'Отменено')], max_length=9, verbose_name='Статус покупки'),
        ),
        migrations.AlterField(
            model_name='shipmentstock',
            name='number',
            field=models.IntegerField(verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='article',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='Артикул'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='warehouse.Category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='number',
            field=models.IntegerField(verbose_name='Количество на складе'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='price',
            field=models.FloatField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='address',
            field=models.TextField(verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='categories',
            field=models.ManyToManyField(related_name='suppliers', through='warehouse.SupplierCategory', to='warehouse.Category'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='contact_info',
            field=models.TextField(null=True, verbose_name='Контактная информация'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='legal_details',
            field=models.TextField(verbose_name='Реквизиты'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='organization',
            field=models.CharField(max_length=80, verbose_name='Организация'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='phone_number',
            field=models.CharField(max_length=20, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='suppliercategory',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='warehouse.Category'),
        ),
        migrations.AlterField(
            model_name='suppliercategory',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='warehouse.Supplier'),
        ),
    ]
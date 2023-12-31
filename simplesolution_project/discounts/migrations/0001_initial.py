# Generated by Django 4.2.3 on 2023-12-28 18:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('payments', '0005_remove_tax_order_delete_discount_delete_tax'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax_amount', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0.01), django.core.validators.MaxValueValidator(100.0)], verbose_name='Налог(%)')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payments.order', verbose_name='Заказ')),
            ],
            options={
                'verbose_name': 'Налог на заказ',
                'verbose_name_plural': 'Налоги на заказ',
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_amount', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0.01), django.core.validators.MaxValueValidator(100.0)], verbose_name='Скидка(%)')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payments.order', verbose_name='Заказ')),
            ],
            options={
                'verbose_name': 'Скидка на заказ',
                'verbose_name_plural': 'Скидки на заказ',
            },
        ),
    ]

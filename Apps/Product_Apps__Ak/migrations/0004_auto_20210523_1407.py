# Generated by Django 3.1.3 on 2021-05-23 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product_Apps__Ak', '0003_auto_20210523_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_products',
            name='discount_percent',
            field=models.IntegerField(blank=True, null=True, verbose_name='درصد تخفیف'),
        ),
    ]
# Generated by Django 2.2.3 on 2019-08-09 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20190809_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordenadas',
            name='x',
            field=models.DecimalField(decimal_places=17, max_digits=20),
        ),
        migrations.AlterField(
            model_name='coordenadas',
            name='y',
            field=models.DecimalField(decimal_places=17, max_digits=20),
        ),
    ]
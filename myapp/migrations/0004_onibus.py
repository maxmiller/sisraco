# Generated by Django 2.2.5 on 2019-09-02 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20190809_1413'),
    ]

    operations = [
        migrations.CreateModel(
            name='Onibus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
            ],
        ),
    ]
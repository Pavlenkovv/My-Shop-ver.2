# Generated by Django 3.1.5 on 2021-02-03 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20210203_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartphone',
            name='sd_volume_max',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name="Максимальний об'єм карти пам'яті"),
        ),
    ]

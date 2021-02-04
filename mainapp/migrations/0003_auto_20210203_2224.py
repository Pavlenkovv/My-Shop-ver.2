# Generated by Django 3.1.5 on 2021-02-03 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_notebook_smartphone'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='for_anonymous_user',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='card',
            name='in_order',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='time_without_charge',
            field=models.CharField(max_length=255, verbose_name='Час автономної роботи'),
        ),
    ]
# Generated by Django 3.2.23 on 2023-11-14 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purityapp', '0008_rename_orderegg_ordered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordered',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]

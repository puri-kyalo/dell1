# Generated by Django 3.2.23 on 2023-11-12 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purityapp', '0005_eggorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='eggorder',
            name='phone',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='eggorder',
            name='delivery_date',
            field=models.DateTimeField(),
        ),
    ]
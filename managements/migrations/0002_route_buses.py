# Generated by Django 4.2.10 on 2024-02-20 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='buses',
            field=models.ManyToManyField(related_name='routes', to='managements.bus'),
        ),
    ]

# Generated by Django 4.2.8 on 2024-02-21 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='arrival_city',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
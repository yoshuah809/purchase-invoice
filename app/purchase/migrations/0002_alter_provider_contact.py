# Generated by Django 3.2.9 on 2022-01-07 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='contact',
            field=models.CharField(max_length=100),
        ),
    ]
# Generated by Django 3.0.7 on 2020-10-11 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20201010_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='rapiest',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]

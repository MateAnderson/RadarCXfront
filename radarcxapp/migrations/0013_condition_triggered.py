# Generated by Django 3.2 on 2021-05-24 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radarcxapp', '0012_auto_20210522_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='condition',
            name='triggered',
            field=models.BooleanField(default=False),
        ),
    ]
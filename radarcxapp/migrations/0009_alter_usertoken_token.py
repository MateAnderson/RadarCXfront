# Generated by Django 3.2 on 2021-05-20 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radarcxapp', '0008_condition_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertoken',
            name='token',
            field=models.CharField(max_length=40),
        ),
    ]
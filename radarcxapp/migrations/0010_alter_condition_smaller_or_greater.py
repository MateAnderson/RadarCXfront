# Generated by Django 3.2 on 2021-05-21 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radarcxapp', '0009_alter_usertoken_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condition',
            name='smaller_or_greater',
            field=models.CharField(max_length=16),
        ),
    ]

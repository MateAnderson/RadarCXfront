# Generated by Django 3.2 on 2021-05-20 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radarcxapp', '0007_alter_condition_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='condition',
            name='name',
            field=models.CharField(default='old', max_length=100),
            preserve_default=False,
        ),
    ]

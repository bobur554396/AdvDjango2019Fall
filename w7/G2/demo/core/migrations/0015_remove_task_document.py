# Generated by Django 2.1.1 on 2019-10-30 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20191030_1044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='document',
        ),
    ]

# Generated by Django 2.1.1 on 2019-09-25 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'DONE'), (2, 'TODO'), (3, 'TESTED')], default=2),
        ),
    ]
# Generated by Django 2.1.1 on 2019-10-30 10:03

from django.db import migrations, models
import utils.upload


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20191030_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='document',
            field=models.FileField(null=True, upload_to=utils.upload.task_document_path),
        ),
    ]

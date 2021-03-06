# Generated by Django 2.1.1 on 2019-10-30 10:44

from django.db import migrations, models
import utils.upload
import utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_task_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='document',
            field=models.FileField(null=True, upload_to=utils.upload.task_document_path, validators=[utils.validators.task_document_extension]),
        ),
    ]

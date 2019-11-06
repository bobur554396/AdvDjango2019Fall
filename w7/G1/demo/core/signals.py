from django.db.models.signals import post_delete
from django.dispatch import receiver

from core.models import Task
from utils.upload import task_delete_path


@receiver(post_delete, sender=Task)
def task_deleted(sender, instance, **kwargs):
    # instance.documents.count() > 0:
    if instance.document:
        task_delete_path(document=instance.document)

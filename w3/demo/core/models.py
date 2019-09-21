from django.db import models
from users.models import MainUser


class Project(models.Model):
    name = models.CharField(max_length=300)
    desc = models.TextField()
    creator = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='projects')

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name
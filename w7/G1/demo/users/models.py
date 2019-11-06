from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser, PermissionsMixin
from django.db import models
from rest_framework.authtoken.models import Token


class MainUser(AbstractUser):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_login}'

    def __str__(self):
        return f'{self.id}: {self.username}'

    def send_greeting_email(self):
        pass

    def send_activate_sms(self):
        pass

    def save(self, *args, **kwargs):
        # pre save
        created = self.pk is None
        super().save(*args, **kwargs)
        # post save
        # if created:
        #     Profile.objects.create(user=self)


class Profile(models.Model):
    user = models.OneToOneField(MainUser, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500)
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.user.username

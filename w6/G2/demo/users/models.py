from django.db import models
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser, PermissionsMixin, BaseUserManager
from rest_framework.authtoken.models import Token


class MainUser(AbstractUser):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_login}'

    def __str__(self):
        # return '%s %s' % (self.id, self.user)
        #
        # return '{0}: {1}'.format(self.id, self.username)
        return f'{self.id}: {self.username}'

# class MainUserManager(BaseUserManager):
#     def _create_user(self, email, password, **extra_fields):
#         if not email:
#             raise ValueError('The given email must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_user(self, email, password, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, password, **extra_fields)
#
#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#
#         return self._create_user(email, password, **extra_fields)


# 3. Substitute by subclassing from AbstractBaseUser
# class MainUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=30, blank=True)
#     last_name = models.CharField(max_length=150, blank=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)
#
#     EMAIL_FIELD = 'email'
#     USERNAME_FIELD = 'user'
#     REQUIRED_FIELDS = []
#
#     objects = MainUserManager()
#
#     class Meta:
#         verbose_name = 'User'
#         verbose_name_plural = 'Users'


# 3. Substitute by subclassing from AbstractUser
# class MainUser(AbstractUser):
#     bio = models.TextField(max_length=500)
#     address = models.CharField(max_length=300)


# 2. Extend with a one-to-one field to User (Profile)

class Profile(models.Model):
    user = models.OneToOneField(MainUser, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500)
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.user.username
# 1. Extending model with proxy model

# class MainUser(User):
#     avatar = models.FileField()
#
#     class Meta:
#         proxy = True
#
#     def get_display_name(self):
#         return self.username[3:]

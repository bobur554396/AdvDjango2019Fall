from django.db import models
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser, PermissionsMixin, BaseUserManager


class MainUser(AbstractUser):
    pass

# 4. Substitute by subclassing from AbstractBaseUser
#
# Main User Manager
# class MainUserManager(BaseUserManager):
#
#     def _create_user(self, phone, password, **extra_fields):
#         if not phone:
#             raise ValueError('The given username must be set')
#         user = self.model(phone=phone, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_user(self, phone, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(phone, password, **extra_fields)
#
#     def create_superuser(self, phone, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#
#         return self._create_user(phone, password, **extra_fields)
#
#
# # Main User Class
# class MainUser(AbstractBaseUser, PermissionsMixin):
#     phone = models.CharField(max_length=10, unique=True)
#     # email = models.EmailField(unique=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#
#     # objects = UserManager()
#
#     EMAIL_FIELD = 'email'
#     USERNAME_FIELD = 'phone'
#     REQUIRED_FIELDS = []
#
#     objects = MainUserManager()
#
#     class Meta:
#         verbose_name = 'User'
#         verbose_name_plural = 'Users'


# 3. Substitute by subclassing from AbstractUser
# class MainUser(AbstractUser):
#     pass


# 2. Extend with a one-to-one field to User (Profile)
class Profile(models.Model):
    bio = models.TextField()
    address = models.TextField()
    user = models.OneToOneField(MainUser, on_delete=models.CASCADE)


# 1. Extending model with proxy model

# class MainUser(User):
#     bio = models.TextField()
#
#     class Meta:
#         proxy = True
#
#
# User.objects.all()
# MainUser.objects.all()


# class Project(models.Model):
#     name = models.CharField(max_length=300)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     class Meta:
#         abstract = True
#
#
# class MyProject(Project):
#     pass

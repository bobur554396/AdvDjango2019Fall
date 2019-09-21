from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import MainUser, Profile


class MyProfile(admin.StackedInline):
    model = Profile
    verbose_name = 'Profile'
    verbose_name_plural = 'Profiles'
    can_delete = False


@admin.register(MainUser)
class MainUserAdmin(UserAdmin):
    inlines = [MyProfile, ]
    list_display = ('id', 'username', 'email')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'bio', 'address')

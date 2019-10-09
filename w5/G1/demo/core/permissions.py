from rest_framework.permissions import IsAuthenticated, BasePermission


class IsDeveloperPermission(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user.is_developer


class CanCreateProjectPermission(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user.is_developer or request.user.is_admin


class CanSomething(BasePermission):
    def has_permission(self, request, view):
        return request.user

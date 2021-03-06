from rest_framework import permissions


class IsAuthorAndStaffOrReadOnly(permissions.BasePermission):
    """
    Доступ для автора, модератора и админа.
    """
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or (
                obj.author == request.user
                or request.user.role == 'admin'
                or request.user.role == 'moderator'
            )
        )


class IsAdminOrSuperuser(permissions.BasePermission):
    """
    Доступ для админа или суперюзера.
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.role == 'admin' or request.user.is_staff
        return False


class AnyReadOnly(permissions.BasePermission):
    """
    Доступ для всех только для чтения.
    """
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class AdminOrReadOnly(permissions.BasePermission):
    """
    Доступ для администратора или только для чтения.
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.role == 'admin' or request.user.is_staff
        return request.method in permissions.SAFE_METHODS

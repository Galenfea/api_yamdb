from rest_framework import permissions

from users.models import ADMIN, MODERATOR
"""Аноним — может просматривать описания произведений, читать отзывы и
комментарии

Аутентифицированный пользователь (user) — может читать
всё, как и Аноним, может публиковать отзывы и ставить оценки произведениям,
может комментировать отзывы; может редактировать и удалять свои
отзывы и комментарии, редактировать свои оценки произведений
Эта роль присваивается по умолчанию каждому новому пользователю

Модератор (moderator) — те же права, что и у Аутентифицированного
пользователя, плюс право удалять и редактировать любые отзывы и комментарии

Администратор (admin) — полные права на управление всем контентом проекта
Может создавать и удалять произведения, категории и жанры. Может назначать
роли пользователям

Суперюзер Django должен всегда обладать правами администратора, пользователя
с правами admin, даже если изменить пользовательскую роль суперюзера — это
не лишит его прав администратора, Суперюзер — всегда администратор, но
администратор — не обязательно суперюзер."""


class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS


class UserPremission(permissions.BasePermission):

    def check_role_premissions(self, request, role):
        if not request.user.is_anonymous:
            return request.user.role == role or request.user.is_superuser

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class Moder(UserPremission):
    def has_object_permission(self, request, view, obj):
        return super().check_role_premissions(request, MODERATOR)


class Admin(UserPremission):
    def has_permission(self, request, view):
        return super().check_role_premissions(request, ADMIN)

    def has_object_permission(self, request, view, obj):
        return super().check_role_premissions(request, ADMIN)

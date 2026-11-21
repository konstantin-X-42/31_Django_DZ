from rest_framework import permissions


class IsModer(permissions.BasePermission):
    # 31 задаем сообщение об ошибке при отказе в доступе
    message = 'Доступ разрешен только пользователям из группы модераторов.'

    def has_permission(self, request, view):
        # 31 проверяем, состоит ли текущий аутентифицированный пользователь в группе moders
        return request.user.groups.filter(name='moders').exists()

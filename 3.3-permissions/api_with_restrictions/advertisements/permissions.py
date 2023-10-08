from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):  # Проверяет права на конкретный объект
        if request.method == 'GET':  # Если в отношении объекта используется метод GET, то проверки прав не надо.
            # Если другие, то проверка соответствия пользователя и разрешённого метода производится.
            return True
        return request.creator == obj.creator
# from functools import wraps
#
#
# def permissions(*perms):
#     @wraps
#     def permission_decorator(func):
#         def wrapper(self, *args, **kwargs):
#             self.permission_classes = perms
#             data = self.func(*args, **kwargs)
#             return data
#         return wrapper
#     return permission_decorator
from rest_framework.response import Response


def permissions(*perms):
    """Не для objects_permissions"""
    def decorator(func):
        def wrapper(self, request, *args, **kwargs):
            # self.permission_classes = perms
            if any(perm.has_permission(self=perm, request=request, view=self) for perm in perms) is False:
                if not request.user or not request.user.is_authenticated:
                    data = Response({'detail': 'Не авторизован'}, status=401)
                else:
                    data = Response({'detail': 'Нет доступа'}, status=403)
            else:
                data = func(self, request, *args, **kwargs)
            return data
        return wrapper
    return decorator


# def permission_classes(*perms):
#     def decorator(func):
#         func.permission_classes = perms
#         return func
#     return decorator

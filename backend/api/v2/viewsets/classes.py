from rest_framework import generics, permissions, mixins, decorators, viewsets


class MixedPermission:
    """Миксин permissions для action"""
    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class MixedPermissionViewSetDS(MixedPermission, viewsets.ViewSet):
    pass


class MixedPermissionGenericViewSetDS(MixedPermission, viewsets.GenericViewSet):
    pass


class CreateUpdateDestroyDS(mixins.CreateModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            MixedPermission,
                            viewsets.GenericViewSet):
    """"""
    pass


class CreateRetrieveUpdateDestroyDS(mixins.CreateModelMixin,
                                    mixins.RetrieveModelMixin,
                                    mixins.UpdateModelMixin,
                                    mixins.DestroyModelMixin,
                                    MixedPermission,
                                    viewsets.GenericViewSet):
    """"""
    pass

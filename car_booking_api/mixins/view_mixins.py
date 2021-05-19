from rest_framework import generics, mixins, status, viewsets


class BaseCreateAPIView(generics.GenericAPIView, mixins.CreateModelMixin, viewsets.Viewset):
    pass


class BaseListAPIView(generics.GenericAPIView, mixins.ListModelMixin, ):
    pass


class BaseRetrieveAPIView(generics.GenericAPIView, mixins.RetrieveModelMixin, ):
    pass


class BaseUpdateAPIView(generics.GenericAPIView, mixins.UpdateModelMixin, ):
    pass


class BaseDeleteAPIView(generics.GenericAPIView, mixins.DestroyModelMixin):
    pass

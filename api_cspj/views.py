from rest_framework import generics
from .models import MyModel, Store, Product
from polls.models import Comment, customuser
from .serializers import *
from .middleware import restrict_access_middleware

class MyModelListCreateAPIView(generics.ListCreateAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

    def dispatch(self, request, *args, **kwargs):
        return restrict_access_middleware(super().dispatch)(request, *args, **kwargs)


class StoreListCreateAPIView(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    def dispatch(self, request, *args, **kwargs):
        return restrict_access_middleware(super().dispatch)(request, *args, **kwargs)


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def dispatch(self, request, *args, **kwargs):
        return restrict_access_middleware(super().dispatch)(request, *args, **kwargs)
    
class UserCreateAPIView(generics.ListCreateAPIView):
    queryset = customuser.objects.all()
    serializer_class = UserSerializer

    def dispatch(self, request, *args, **kwargs):
        return restrict_access_middleware(super().dispatch)(request, *args, **kwargs)
    
class CommentCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def dispatch(self, request, *args, **kwargs):
        return restrict_access_middleware(super().dispatch)(request, *args, **kwargs)

class CommentDetailAPIView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDeleteAPIView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def dispatch(self, request, *args, **kwargs):
        return restrict_access_middleware(super().dispatch)(request, *args, **kwargs)

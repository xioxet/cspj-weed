from rest_framework import generics
from .models import MyModel, Store, Product
from polls.models import Comment
from .serializers import MyModelSerializer, StoreSerializer, ProductSerializer, CommentSerializer
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
    

class CommentCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def dispatch(self, request, *args, **kwargs):
        return restrict_access_middleware(super().dispatch)(request, *args, **kwargs)

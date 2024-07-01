from rest_framework import generics
from .models import MyModel, Store, Product
from .serializers import MyModelSerializer, StoreSerializer, ProductSerializer
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

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MyModel, Store, Product
from polls.models import Comment, customuser
from .serializers import *
from .middleware import restrict_access_middleware
from django.shortcuts import render, redirect

from asgiref.sync import async_to_sync
import requests

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

class SSRFView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SSRFSerializer(data=request.data)
        if serializer.is_valid():
            url = serializer.data["request"]
            print(url, type(url))
            data = self.get_request(url)
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @async_to_sync
    async def get_request(self, request):
        return requests.get(request)
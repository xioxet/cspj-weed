from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MyModel, Store, Product
from polls.models import Comment, customuser
from .serializers import *
from .middleware import restrict_access_middleware
from django.db import connection
from asgiref.sync import async_to_sync
import requests
import json

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
        print(request.data)
        serializer = SSRFSerializer(data=request.data)
        if serializer.is_valid():
            url = serializer.data["request"]
            if "forbidden" in url:
                return Response({'request':'Forbidden 403'})
            data = self.get_request(url)
            print(data)
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @async_to_sync
    async def get_request(self, request):
        return requests.get(request).json()
    
class SQLIView(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = SQLISerializer(data=request.data)
        if serializer.is_valid():
            with connection.cursor() as cursor:
                    cursor.execute(serializer.data['request'].split("'")[-1])
                    row_headers = [x[0] for x in cursor.description]
                    rv = cursor.fetchall()
                    json_data = []
                    for result in rv:
                        json_data.append(dict(zip(row_headers, result)))
                    # filter out datetimes
                    return Response(json_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
# myapp/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('mymodels/', MyModelListCreateAPIView.as_view(), name='mymodel-list-create'),
    path('stores/', StoreListCreateAPIView.as_view(), name='store-list-create'),
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('comments/', CommentCreateAPIView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetailAPIView.as_view(), name='comment-detail'),
    path('comments/<int:pk>/delete/', CommentDeleteAPIView.as_view(), name='comment-delete'),
    path('users/', UserCreateAPIView.as_view(), name='user-list-create'),
    path('ssrfapi/', SSRFView.as_view(), name='ssrf-view'),
    path('sqliapi/', SQLIView.as_view(), name='sqli-view'),
]

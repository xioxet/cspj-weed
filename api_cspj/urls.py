# myapp/urls.py

from django.urls import path
from .views import MyModelListCreateAPIView, StoreListCreateAPIView, ProductListCreateAPIView, CommentCreateAPIView

urlpatterns = [
    path('mymodels/', MyModelListCreateAPIView.as_view(), name='mymodel-list-create'),
    path('stores/', StoreListCreateAPIView.as_view(), name='store-list-create'),
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('comments/', CommentCreateAPIView.as_view(), name='comment-list-create'),
]

# myapp/urls.py

from django.urls import path
from .views import MyModelListCreateAPIView

urlpatterns = [
    path('mymodels/', MyModelListCreateAPIView.as_view(), name='mymodel-list-create'),
]

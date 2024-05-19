from django.urls import path
from .views import upload_file
from . import views

app_name = 'polls'

urlpatterns = [
    path("", views.index, name="index"),
    path('upload/', upload_file, name='upload_file'),
]


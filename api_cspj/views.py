# myapp/views.py

from rest_framework import generics
from .models import MyModel
from .serializers import MyModelSerializer
from .middleware import restrict_access_middleware

class MyModelListCreateAPIView(generics.ListCreateAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

    def dispatch(self, request, *args, **kwargs):
        # Apply the middleware only to this view
        return restrict_access_middleware(super().dispatch)(request, *args, **kwargs)

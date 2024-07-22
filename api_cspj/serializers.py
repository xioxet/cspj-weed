# myapp/serializers.py

from rest_framework import serializers
from .models import MyModel, Store, Product
from polls.models import Comment, customuser

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    store = StoreSerializer(read_only=True)
    store_id = serializers.PrimaryKeyRelatedField(
        queryset=Store.objects.all(), source='store', write_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text', 'user']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = customuser
        fields = '__all__'
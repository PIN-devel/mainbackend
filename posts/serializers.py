from rest_framework import serializers
from .models import Post
from users.serializers import UserSerializer


class ListPostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'created_at', 'updated_at',]
        read_only_fields = ['author']


class DetailPostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['author']

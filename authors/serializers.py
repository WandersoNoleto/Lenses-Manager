from rest_framework import serializers


class AuthorSerializer(serializers.Serializer):
    author = serializers.CharField(max_length=255)
    bio    = serializers.CharField(max_length=255)
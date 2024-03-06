from rest_framework import serializers

class TagSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    
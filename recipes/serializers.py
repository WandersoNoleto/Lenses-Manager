from rest_framework import serializers
from recipes.models import Category
from tags.serializers import TagSerializer
from tags.models import Tag

class RecipeSerializer(serializers.Serializer):
    id          = serializers.IntegerField()
    title       = serializers.CharField(max_length=255) 
    description = serializers.CharField(max_length=255) 
    preparation = serializers.SerializerMethodField()
    category    = serializers.StringRelatedField()
    author      = serializers.StringRelatedField()
    tags        = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True, write_only=True)
    tags_name   = TagSerializer(source='tags', many=True)
    
    def get_preparation(self, recipe):
        return f'{recipe.preparation_time} {recipe.preparation_time_unit}'
from rest_framework import serializers

class RecipeSerializer(serializers.Serializer):
    id          = serializers.IntegerField()
    title       = serializers.CharField(max_length=255) 
    description = serializers.CharField(max_length=255) 
    preparation = serializers.SerializerMethodField()
    category    = serializers.StringRelatedField()
    author      = serializers.StringRelatedField()
    tags_name   = serializers.SerializerMethodField()
    
    def get_preparation(self, recipe):
        return f'{recipe.preparation_time} {recipe.preparation_time_unit}'
    
    def get_tags_name(self, recipe):
        return [tag.name for tag in recipe.tags.all()]
from rest_framework import serializers
from collections import defaultdict

from attr import attr

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
    
    def validate(self, attrs):
        super_validate = super().validate(attrs)

        title = attrs.get('title')
        description = attrs.get('description')

        if title == description:
            raise serializers.ValidationError(
                {
                    "title": ["Posso", "ter", "mais de um erro"],
                    "description": ["Posso", "ter", "mais de um erro"],
                }
            )

        return super_validate

    def validate_title(self, value):
        title = value

        if len(title) < 5:
            raise serializers.ValidationError('Must have at least 5 chars.')

        return title
    def get_tags_name(self, recipe):
        return [tag.name for tag in recipe.tags.all()]
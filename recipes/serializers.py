from rest_framework import serializers
from authors.validators import AuthorRecipeValidator
from recipes.models import Recipe

from attr import attr

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Recipe
        fields = [
            'id', 'title', 'description', 'author',
            'category', 'tags', 'preparation',
            'preparation_steps', 'serving', 'tags_name'
        ]
    
    
    preparation = serializers.SerializerMethodField()
    serving     = serializers.SerializerMethodField()
    category    = serializers.StringRelatedField()
    author      = serializers.StringRelatedField()
    tags_name   = serializers.SerializerMethodField()
    
    def get_preparation(self, recipe):
        return f'{recipe.preparation_time} {recipe.preparation_time_unit}'
    
    def get_serving(self, recipe):
        return f'{recipe.servings} {recipe.servings_unit}'
    
    def validate(self, attrs):
        super_validate = super().validate(attrs)

        validator = AuthorRecipeValidator(data=self.initial_data, ErrorClass=serializers.ValidationError)
        validator.clean()

        return super_validate


        return title
    def get_tags_name(self, recipe):
        return [tag.name for tag in recipe.tags.all()]
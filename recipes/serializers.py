from authors.validators import AuthorRecipeValidator
from rest_framework import serializers

from tags.serializers import TagSerializer
from recipes.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = [
            'id', 'title', 'description', 'author',
            'public', 'category', 'tags', 'preparation',
            'tag_objects', 'preparation_time', 'preparation_time_unit', 
            'servings', 'servings_unit',
            'preparation_steps', 'cover'
        ]

    public      = serializers.BooleanField(source='is_published',read_only=True)
    preparation = serializers.SerializerMethodField(read_only=True)
    category    = serializers.StringRelatedField(read_only=True)
    tag_objects = TagSerializer(many=True, source='tags',read_only=True)


    def get_preparation(self, recipe):
        return f'{recipe.preparation_time} {recipe.preparation_time_unit}'
    
    def validate(self, attrs):
        if self.instance is not None and attrs.get('servings') is None:
            attrs['servings'] = self.instance.servings

        if self.instance is not None and attrs.get('preparation_time') is None:
            attrs['preparation_time'] = self.instance.preparation_time

        super_validate = super().validate(attrs)
        AuthorRecipeValidator(
            data=attrs,
            ErrorClass=serializers.ValidationError,
        )
        return super_validate

    def save(self, **kwargs):
        return super().save(**kwargs)

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
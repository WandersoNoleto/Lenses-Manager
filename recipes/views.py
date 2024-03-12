from recipes.models import Recipe
from recipes.serializers import RecipeSerializer
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend


class RecipeAPIViewSet(ModelViewSet):
    queryset         = Recipe.objects.get_published()
    serializer_class = RecipeSerializer
    filter_backends  = [DjangoFilterBackend]
    filterset_fields = ['category', 'tags']
    
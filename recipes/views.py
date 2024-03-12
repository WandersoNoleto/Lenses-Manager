from recipes.models import Recipe
from recipes.serializers import RecipeSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView


class RecipeList(ListCreateAPIView):
    queryset         = Recipe.objects.get_published()
    serializer_class = RecipeSerializer


class RecipeDetail(RetrieveUpdateAPIView):
    queryset         = Recipe.objects.get_published()
    serializer_class = RecipeSerializer
        
from recipes.models import Recipe
from recipes.serializers import RecipeSerializer
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from recipes.permissions import IsOwner
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class RecipeAPIViewSet(ModelViewSet):
    queryset         = Recipe.objects.all() 
    serializer_class = RecipeSerializer
    filter_backends  = [DjangoFilterBackend]
    filterset_fields = ['category', 'tags']
    permission_classes = [IsAuthenticatedOrReadOnly]
    http_method_names  = ['get', 'options', 'head', 'patch', 'post', 'delete']
    
        
    def get_permissions(self):
        if self.request.method in ['PATCH', 'ṔOST']:
            return [IsOwner(),]
        
        return super().get_permissions()
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        
        headers = self.get_success_headers(serializer.data)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def get_queryset(self):
        only_published = self.request.query_params.get('only_published', None)

        queryset = super().get_queryset()

        if only_published and only_published.lower() == 'true':
            queryset = Recipe.objects.get_published()

        return queryset

        
    
    def publish_recipe(self, request, pk, *args, **kwargs):
        recipe = get_object_or_404(Recipe, pk=pk)
        recipe.is_published = True
        recipe.save()
        
        serializer = self.get_serializer(recipe)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
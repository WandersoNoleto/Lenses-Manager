from recipes.models import Recipe
from recipes.serializers import RecipeSerializer
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from recipes.permissions import IsOwner
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework.response import Response

class RecipeAPIViewSet(ModelViewSet):
    queryset         = Recipe.objects.get_published()
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
    
from rest_framework.viewsets import ModelViewSet
from authors.serializers import AuthorSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import action

class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    
    def get_queryset(self):
        User     = get_user_model()
        queryset = User.objects.all()
        return queryset
    
    @action(methods=['get'], detail=False)
    def me(self, request, *args, **kwargs):
        obj        = self.get_queryset().first()
        serializer = self.get_serializer(
            instance=obj
        )
        
        return Response(serializer.data)
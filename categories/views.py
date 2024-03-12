from categories.serializers import CategorySerializer
from rest_framework.viewsets import ModelViewSet
from categories.models import Category

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names  = ['get', 'options', 'head', 'patch', 'post', 'delete']

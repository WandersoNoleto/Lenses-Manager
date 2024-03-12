from tags.serializers import TagSerializer
from rest_framework.viewsets import ModelViewSet
from tags.models import Tag

class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    http_method_names  = ['get', 'options', 'head', 'patch', 'post', 'delete']

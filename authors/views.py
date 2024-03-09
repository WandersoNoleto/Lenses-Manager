from rest_framework.decorators import api_view
from rest_framework.response import Response
from authors.models import Profile
from authors.serializers import AuthorSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status

@api_view(http_method_names=['get', 'post'])
def author_list(request):
    if request.method == 'GET':     
        authors    = Profile.objects.all()[:10]
        serializer = AuthorSerializer(instance=authors, many=True)
        return Response(serializer.data)
    
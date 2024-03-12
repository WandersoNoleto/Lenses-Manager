from rest_framework.routers import SimpleRouter
from . import views

app_name = 'tags'

tag_router = SimpleRouter()
tag_router.register(prefix='',viewset=views.TagViewSet, basename='tag')

urlpatterns = tag_router.urls
from rest_framework.routers import SimpleRouter
from . import views

author_router = SimpleRouter()
author_router.register(prefix='api', viewset=views.AuthorViewSet, basename='author-api')

urlpatterns = author_router.urls
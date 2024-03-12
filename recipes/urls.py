
from django.urls import path, include
from recipes import views
from rest_framework.routers import SimpleRouter

app_name = 'recipes'
recipe_router = SimpleRouter()
recipe_router.register(
    'recipes',
    views.RecipeAPIViewSet,
)

urlpatterns = [
    path('', include(recipe_router.urls))
]

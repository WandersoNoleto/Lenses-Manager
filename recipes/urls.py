
from django.urls import path, include
from recipes import views
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

app_name = 'recipes'
recipe_router = SimpleRouter()
recipe_router.register(
    'recipes',
    views.RecipeAPIViewSet,
)

urlpatterns = [
    path('', include(recipe_router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

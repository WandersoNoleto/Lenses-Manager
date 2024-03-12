from rest_framework.routers import SimpleRouter
from . import views

app_name = 'categories'

category_router = SimpleRouter()
category_router.register(prefix='',viewset=views.CategoryViewSet, basename='category')

urlpatterns = category_router.urls
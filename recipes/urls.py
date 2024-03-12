
from django.urls import path
from recipes import views


urlpatterns = [
    path('', views.RecipeList.as_view(), name='recipes_list'),
    path('<int:pk>/', views.RecipeDetail.as_view(), name='recipe_detail')
]

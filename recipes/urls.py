
from django.urls import path
from recipes import views


urlpatterns = [
    path('', views.recipe_list, name='recipes_list'),
    path('<int:pk>/', views.recipe_detail, name='recipe_detail')
]

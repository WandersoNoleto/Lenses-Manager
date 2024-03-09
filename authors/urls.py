from django.urls import path
from authors import views


urlpatterns = [
    path('', views.author_list, name='authors_list'),
]

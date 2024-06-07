from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', DetailTodo.as_view()),
    path('', ListTodo.as_view()),
    path('create/', CreateTodo.as_view()),
    path('<int:pk>/delete/', DeleteTodo.as_view())
]

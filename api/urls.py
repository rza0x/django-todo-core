from django.urls import path
from .views import (
    TodoListCreateAPIView,
    TodoRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path("todos/", TodoListCreateAPIView.as_view(), name="api_todo_list_create"),
    path(
        "todos/<int:pk>/",
        TodoRetrieveUpdateDestroyAPIView.as_view(),
        name="api_todo_detail",
    ),
]

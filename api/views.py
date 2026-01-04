from rest_framework import generics, permissions
from todo.models import Todo
from .serializers import TodoSerializer


class TodoListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TodoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)


# {
#     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc2ODA5MzcxMywiaWF0IjoxNzY3NDg4OTEzLCJqdGkiOiI2NGU5NjJiM2VhNjA0MzFkOThkM2I2MTU2MDhhODhkZiIsInVzZXJfaWQiOiIxIn0.2DfyTPhJ1k3dZAsQZIY8ksprYQVIRhyocnflp-p6DpQ",
#     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzY3NDkwNzEzLCJpYXQiOjE3Njc0ODg5MTMsImp0aSI6IjNiZjY3NWE4YzUxYTRjZGFiNjgxYzVjMTc4MDc3MjY0IiwidXNlcl9pZCI6IjEifQ.QBOsEJ4lgwznTQGfrG5-XrB7-BtaBrLRDuckl8akJpY"
# }

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Todo
from .forms import TodoForm


class TodoListView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = "todo/todo_list.html"
    context_object_name = "todos"

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    form_class = TodoForm
    template_name = "todo/todo_form.html"
    success_url = reverse_lazy("todo_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = "todo/todo_form.html"
    success_url = reverse_lazy("todo_list")

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)


class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = Todo
    template_name = "todo/todo_confirm_delete.html"
    success_url = reverse_lazy("todo_list")

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

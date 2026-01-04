from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Title"}),
        label="Title",
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Description (optional)",
                "rows": 3,
            }
        ),
        required=False,
        label="Description",
    )
    is_completed = forms.BooleanField(
        required=False,
        label="Completed",
    )

    class Meta:
        model = Todo
        fields = ["title", "description", "is_completed"]

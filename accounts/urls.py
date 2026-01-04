from django.urls import path
from .views import CustomLoginView, SignUpView, CustomLogoutView

urlpatterns = [
    path("", CustomLoginView.as_view(), name="login"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
]

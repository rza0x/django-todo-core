from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import SignUpForm, CustomAuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View


class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
    authentication_form = CustomAuthenticationForm
    redirect_authenticated_user = True


class SignUpView(FormView):
    template_name = "accounts/signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CustomLogoutView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect("login")

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("login")

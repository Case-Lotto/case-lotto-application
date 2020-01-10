from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from app import forms
from django.views.generic import FormView
from app.models import Wallet, Case, Profile

# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, "home.html")

class DailyCase(View):
    def get(self, request):
        return render(request, "daily-case.html")

class CoinFlip(View):
    def get(self, request):
        return render(request, "coin-flip.html")

class About(View):
    def get(self, request):
        return render(request, "about.html")

class SignUpView(FormView):
    form_class = forms.SignUpForm
    template_name = "auth/user_form.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        user = form.signup()
        login(self.request, user)
        return super().form_valid(form)

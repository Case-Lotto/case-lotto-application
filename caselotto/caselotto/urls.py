from django.contrib import admin
from django.urls import path, include
from app.views import Home, DailyCase, CoinFlip, About, SignUpView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", Home.as_view(), name="home"),
    path("daily-case", DailyCase.as_view(), name="daily-case"),
    path("coin-flip", CoinFlip.as_view(), name="coin-flip"),
    path("about", About.as_view(), name="about"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("sign-up/", SignUpView.as_view(), name="sign-up"),
]

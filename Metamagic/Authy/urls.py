from django.urls import path, include
from django.conf.urls import include
from . import views
from django.contrib.auth import views as auth_views

app_name = "Authy"

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),

    # reset password urls#######
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]
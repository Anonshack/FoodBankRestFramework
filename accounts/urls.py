from .views import (
    LogoutView,
    RegisterView, 
    ProfileView, 
    ImageUpdateView,
    CustomAuthToken
)
from django.urls import path
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

urlpatterns = [
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('register/', RegisterView.as_view(), name='register'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),

    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('password_reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/picture/', ImageUpdateView.as_view(), name='update_image'),
]

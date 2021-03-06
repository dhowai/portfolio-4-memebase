from django.urls import path
from .views import (
    UserRegisterView, EditUserDetailsView,
    PasswordsChangeView, ProfilePageView,
    EditProfilePageView, CreateProfilePageView)

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_user_details/', EditUserDetailsView.as_view(
        ), name='edit_user_details'),
    path('password/', PasswordsChangeView.as_view(
        template_name='registration/change_password.html'
        ), name="change_password"),
    path('<int:pk>/profile/', ProfilePageView.as_view(), name='profile_page'),
    path('<int:pk>/edit_profile/', EditProfilePageView.as_view(
        ), name='edit_profile_page'),
    path('create_profile_page/', CreateProfilePageView.as_view(
        ), name='create_profile_page'),
]

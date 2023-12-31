# users/urls.py
from django.urls import path
from .views import CreateAccountView,UserProfileView


app_name ='users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('profile/', UserProfileView.as_view(), name='userProfile'),
]


from django.urls import path
from .views import UserRegistration, UserLoginView

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login')
]
from django.urls import path
from .views import signup_view, login_view, logout_view

urlpatterns = [
    path('signup/', signup_view, name='UserSignup'),
    path('login/', login_view, name='UserLogin'),
    path('logout/', logout_view, name='UserLogout'),
]

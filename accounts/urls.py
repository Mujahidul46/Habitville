from django.urls import path
from .views import signup_view, login_view, logout_view, user_profile_view, verify_session

urlpatterns = [
    path('signup/', signup_view, name='UserSignup'),
    path('login/', login_view, name='UserLogin'),
    path('logout/', logout_view, name='UserLogout'),
    path('profile/', user_profile_view, name='UserProfile'),
    path('verify-session/', verify_session, name='verify-session'),
]

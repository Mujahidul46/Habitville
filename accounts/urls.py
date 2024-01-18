from django.urls import path
from .views import signup_view

# tells django which views to invoke when a specific URL is requested by the user. Use name to refer to each path elsewhere in code.
urlpatterns = [
    path('signup/', signup_view, name='UserSignup'),
]

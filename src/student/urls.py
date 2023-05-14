from django.urls import path
from .views import StudentIndexView, LoginView, ProfileView

app_name = 'student'

urlpatterns = [
    path("", StudentIndexView.as_view(), name='index'),
    path("login", LoginView.as_view(), name='login'),
    path("profile", ProfileView.as_view(), name='profile')
]

from django.urls import path
from .views import UniversityIndexView, LoginView

app_name = 'university'

urlpatterns = [
    path("", UniversityIndexView.as_view(), name='index'),
    path("login", LoginView.as_view(), name='login')
]

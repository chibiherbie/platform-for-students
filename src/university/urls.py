from django.urls import path
from .views import UniversityIndexView

app_name = 'university'

urlpatterns = [
    path("", UniversityIndexView.as_view(), name='index')
]

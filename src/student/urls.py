from django.urls import path
from .views import StudentIndexView

app_name = 'student'

urlpatterns = [
    path("", StudentIndexView.as_view(), name='index')
]

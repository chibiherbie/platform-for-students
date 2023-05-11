from django.urls import path
from .views import student_index

app_name = 'student'

urlpatterns = [
    path("", student_index, name='index')
]

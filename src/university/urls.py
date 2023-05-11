from django.urls import path
from .views import university_index

app_name = 'university'

urlpatterns = [
    path("", university_index, name='index')
]

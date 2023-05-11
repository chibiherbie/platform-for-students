from django.shortcuts import render
from django.http import HttpResponse


def university_index(request):
    return HttpResponse("university")

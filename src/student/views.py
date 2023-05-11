from django.shortcuts import render
from django.http import HttpResponse


def student_index(request):
    return HttpResponse("student")

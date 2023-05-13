from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views import View


class UniversityIndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'university/university-index.html')


class LoginView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'university/login.html')

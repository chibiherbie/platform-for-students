from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views import View


class StudentIndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'student/student-index.html')

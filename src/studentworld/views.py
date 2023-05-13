from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views import View


class StudentWorldIndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'studentworld/student-world-index.html')

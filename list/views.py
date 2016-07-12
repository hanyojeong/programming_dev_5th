from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'list/index.html')
    #return HttpResponse("한효정의 자기소개 페이지에 오신 것을 환영합니다^^")
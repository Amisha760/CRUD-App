from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("hi")
def add_show(request):
    return render(request,'enroll/addandshow.html')
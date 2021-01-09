from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("home Index")
def FAQ(request):
    return render(request,'prediction/faq.html')

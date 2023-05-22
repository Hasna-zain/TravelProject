from django.shortcuts import render
from django.http import HttpResponse
from .models import place
from .models import team
# Create your views here.

def index(request):
    obj=place.objects.all()
    obj1=team.objects.all()
    return render(request,'index.html',{'res':obj,'result':obj1})
def demo(request):
    n='india'
    return render(request,'demo.html',{'obj':n})
def about(request):
    return render(request,'about.html')
def contact(request):
    return HttpResponse("it is contact page")
def addition(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    r=x+y
    return render(request,'results.html',{'res':r})
from django.http import HttpResponse
from django.shortcuts import render
def about(request):
    return HttpResponse("This is about page")

def Home(request):
    return render(request,'home.html',{'greeting':'Hello!'})
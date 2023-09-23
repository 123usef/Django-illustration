from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


#function base view -->
#class base view --> 

def home(request):
    #do some logic 
    todos = todo.objects.get(id=1) #select * from todo  
    return HttpResponse(todos.name)


def profile(request):
    
    return HttpResponse("welcome in profile")
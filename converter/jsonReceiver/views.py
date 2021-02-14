from django.shortcuts import render
from django.http import HttpResponse
from .models import Files
import os

from django.conf import settings



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    
def app_save(request):
    if request.method == 'POST':
        newdoc = Files(json_file=request.FILES.get('myfile'))
        newdoc.save()
        return HttpResponse("File Saved Succesfully")
       

   
    
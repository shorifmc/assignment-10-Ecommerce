from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def getContact(request):
    return render(request,'Cloth/shirt.html')
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cloth(request):
    return render(request,'Cloth/shirt.html')

def getShirt(request):
    return render(request,'Cloth/shirt.html')

def getPant(request):
    return render(request,'Cloth/pant.html')

def getTshirt(request):
    return render(request,'Cloth/tshirt.html')


def getReg(request):
    return render(request,'Cloth/regform.html')
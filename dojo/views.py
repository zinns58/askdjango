from django.http import HttpResponse
from django.shortcuts import render

def mysum(request, x, y=0, z=0):
    return HttpResponse(x + y + z)

def mysum2(request, numbers):
    result = sum(map(lambda s: int(s or 0), numbers.split("/")))
    return HttpResponse(result)
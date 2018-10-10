from django.http import HttpResponse
from django.shortcuts import render

def mysum(request, x, y=0, z=0):
    return HttpResponse(x + y + z)
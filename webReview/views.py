from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse


# from .models import
def home(request):
    return HttpResponse('admin')

# Create your views here.

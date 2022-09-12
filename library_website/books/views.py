from django.http import HttpResponse
from django.shortcuts import render

from .models import Book


def index(request):
    return HttpResponse("You're at the index.")

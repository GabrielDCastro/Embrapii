from django.shortcuts import render
from .models import Cliente
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

def home(requests):
    clientes = Cliente.objects.all()
    return render(requests, 'home.html', {'clientes': clientes})
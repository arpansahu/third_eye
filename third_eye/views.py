from django.shortcuts import render, redirect

def home(request):
    return render(request, 'index.html')

def particles(request):
    return render(request, 'table1.html')
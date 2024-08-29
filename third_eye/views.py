from django.shortcuts import render, redirect

def home(request):
    return render(request, 'base.html')

def particles(request):
    return render(request, 'table1.html')

def error_404(request, exception):
    return render(request, 'error/error_404.html')


def error_400(request, exception):
    return render(request, 'error/error_400.html')


def error_403(request, exception):
    return render(request, 'error/error_403.html')


def error_500(request):
    return render(request, 'error/error_500.html')
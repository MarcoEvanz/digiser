from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')
def insert(request):
    return render(request, 'pages/insert.html')
def check(request):
    return render(request, 'pages/check.html')
def support(request):
    return render(request, 'pages/support.html')
def system(request):
    return render(request, 'pages/system.html')
def wiki(request):
    return render(request, 'pages/wiki.html')
def courses(request):
    return render(request, 'pages/courses.html')
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def what(request):
    return render(request, 'what.html')

def about(request):
    return render(request, 'about_us.html')

def login(request):
    return render(request, 'Login.html')

def contact(request):
    return render(request, 'contact.html')
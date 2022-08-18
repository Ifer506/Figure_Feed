from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .models import review
# from forms import Contact
# Create your views here.

def home(request):
    return render(request, 'index.html',{'review' : review})

def what(request):
    return render(request, 'what.html')

def about(request):
    return render(request, 'about_us.html')

def login(request):
    return render(request, 'Login.html')

def signin(request):
    if request.method == "POST":
        print("this is done")
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = request.POST['User']
            email = request.POST['Email']
            password = request.POST['Password']
            print(user,email,password)
            # ins = signin(user=user, email=email , password = password)
            # ins.save()
            form.save()
    
    return render(request, 'Login.html')


     

def contact_views(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("this is done")
            # customer_name = request.POST['customer_name']
            # phone = request.POST['phone']
            # email = request.POST['customer_email']
            # message = request.POST['message']
            # print(customer_name,phone,email,message)
            # ins = contact_views(name=customer_name, phone=phone , email=email , message = message)
            form.save()

    return render(request, 'contact.html')


def review(request):
    review = review.objects.all()
    return render(request, 'index.html',{'review' : review})
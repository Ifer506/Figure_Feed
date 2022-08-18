from django.urls import path
from django.views.generic import RedirectView
from .import views

urlpatterns = [
    path('',views.home , name = "home"),
    path('what',views.what , name = "what"),
    path('about',views.about , name = "about"),
    path('signin',views.login , name = "login"),
    path('signin',views.signin , name = "signin"),
    path('contact',views.contact_views , name = "contact"),
    path('',views.review , name = "review"),
    
]
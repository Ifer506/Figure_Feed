from django.urls import path
from .import views

urlpatterns = [
    path('',views.home , name = "home"),
    path('what/',views.what , name = "what"),
    path('about/',views.about , name = "about"),
    path('login/',views.login , name = "login"),
    path('contact/',views.contact , name = "contact"),
]
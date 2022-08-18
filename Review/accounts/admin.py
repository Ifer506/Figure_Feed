from django.contrib import admin
from accounts.models import SignUp
from .models import contact, review

# Register your models here.
class SignUpadmin(admin.ModelAdmin):
    list_display = ('username','email' , 'password','password')

admin.site.register(SignUp,SignUpadmin)

# class Contactadmin(admin.ModelAdmin):
#     list_display = ('messageId', 'name' ,'phone' ,'email' , 'message')

# admin.site.register(contact,Contactadmin)
admin.site.register(contact)

admin.site.register(review)
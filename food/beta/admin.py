from django.contrib import admin
from beta.models import SignUp

# Register your models here.



class SignUpadmin(admin.ModelAdmin):
    list_display = ('username','email' , 'password')

admin.site.register(SignUp,SignUpadmin)
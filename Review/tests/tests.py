from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from accounts.views import login,about,contact,home
from django.contrib.auth import get_user_model
from accounts.views import about
from accounts.views import order as orderPr

# Create your tests here.
class TestUrls(SimpleTestCase):
    def test_login_page_url(self):
        url = reverse(login)
        print(url)
        self.assertEquals(resolve(url).func,login)

    def test_contact_url(self):
        url = reverse(contact)
        print(url)
        self.assertEquals(resolve(url).func,contact)

    def test_admin_home_url(self):
        url = reverse(home)
        print(url)
        self.assertEquals(resolve(url).func,home)

    
    
    def test_admin_home_Render(self):
        url = reverse(home)
        print(url)
        self.assertEquals(resolve(url).func,home)

User = get_user_model
class TestViews(TestCase):

    
      
    def test_admin_login(self):
        url = reverse(login)
        response= self.assertEquals(resolve(url).func,login)
        self.assertTemplateUsed(response, 'admin/admin_login.html')
    
          
    def test_contact(self):
        url = reverse(contact)
        response= self.assertEquals(resolve(url).func,contact)
        self.assertTemplateUsed(response, 'admin/admin_contact.html')
        
           
    def test_about(self):
        url = reverse(about)
        response= self.assertEquals(resolve(url).func,about)
        self.assertTemplateUsed(response, 'about.html')

          

           
    



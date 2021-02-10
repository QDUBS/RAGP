from django.urls import path
from .views import Home, ContactUs, AboutUs, BizInfo




urlpatterns = [
   path('home/', Home, name = 'home'),
   path('contact/', ContactUs, name = 'contact'),
   path('about/', AboutUs, name = 'about'),
   path('bizinfo/', BizInfo, name = 'bizinfo'),
]


from django.urls import path
from portfolio import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('handleblog',views.handleblog,name='handleblog'),
    path('resume',views.resume,name='resume'),
    path('service',views.service,name='service'),
    
]
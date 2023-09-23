from django.urls import path
from . import views

#3skri eshart mror 
#cycle :
#request(localhost:8000?/home) --> 3skri --> urls list 
urlpatterns = [
    path('' , views.home , name='home'),
    path('profile/' , views.profile , name='profile'),
    
]
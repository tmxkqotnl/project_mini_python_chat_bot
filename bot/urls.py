from django.urls import path 
from . import views

urlpatterns = [ 
    path('' , views.Login.as_view() , name='login')
    # path('login',,name='login')
]
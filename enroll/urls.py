from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.add_show,name='add_show'),
    
  
]
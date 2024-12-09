from django.urls import path
from .views import *
urlpatterns = [
    path('signup/',signup,name='signup'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('dashboard/',dashboard,name='dashboard'),
    path('singlestudentdetails/<reg>/',singlestudentdetails,name='singlestudentdetails'), 
    path('delete/<reg>',delete,name='delete'),
]
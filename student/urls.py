from django.urls import path
from student.views import *
urlpatterns = [
    path('',home,name='home'),
    path('aboutus/',aboutus,name='aboutus'),
    path('registration/',registration,name='registration'),
    path('python/',python,name='python'),
    path('java/',java,name='java'),
    path('aws/',aws,name='aws'),
    path('placement/',placement,name='placement'),
]
from django.db import models

# Create your models here.
class Placed_student(models.Model):
    photo=models.ImageField(upload_to='photo/%Y/%m/%d/')
    name = models.CharField(max_length=255, default='default_name')
    designation=models.CharField(max_length=50)
    company=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
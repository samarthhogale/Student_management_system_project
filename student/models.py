from django.db import models

# Create your models here.
class Student_details(models.Model):
    reg_no=models.AutoField(primary_key=True,auto_created=True)
    name=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    email=models.EmailField(null=True)
    degree=models.CharField(max_length=100)
    percentage=models.FloatField()
    course=models.CharField(max_length=100)
    fee=models.FloatField()
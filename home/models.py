from django.db import models

# Create your models here.
class Contact(models.Model):
    email= models.CharField(max_length=130)
    password= models.CharField(max_length=130)
    address=models.CharField(max_length=130)
    city=models.CharField(max_length=130)
    date=models.DateField()

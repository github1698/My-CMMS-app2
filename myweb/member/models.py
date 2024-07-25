from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField( max_length=50)
    fname=models.CharField( max_length=50, default="")
    lname=models.CharField(max_length=50, default="")
    email=models.EmailField( max_length=254)
    pass1=models.CharField( max_length=50)
    pass2=models.CharField( max_length=50)

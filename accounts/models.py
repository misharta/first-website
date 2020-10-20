from django.db import models

# Create your models here.
class  mycustomers(models.Model):
    name = models.CharField(max_length=100)
    accountnumber = models.IntegerField()
    CurrentBalance = models.IntegerField() 
    emailid = models.CharField(max_length= 100)
    
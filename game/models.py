from django.db import models

# Create your models here.

class palindrome(models.Model):
    string=models.CharField(max_length=6,default="")
    user=models.CharField(max_length=20)

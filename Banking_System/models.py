from django.db import models

# Create your models here.
class Cutomers(models.Model):
    name=models.CharField(max_length=50,default=None)
    email=models.EmailField()
    phone_no=models.IntegerField()
    balance=models.FloatField()

class History(models.Model):
    transfered_by=models.CharField(max_length=50,default=None)
    transfered_to=models.CharField(max_length=50,default=None)
    amount=models.FloatField(default=0)





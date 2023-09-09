from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    name=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    mobile_no=models.IntegerField(null=True,blank=True)
    status=models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name.username
class Message(models.Model):
    msg=models.CharField(max_length=300,null=True,blank=True)
    sender=models.CharField(max_length=30,null=True,blank=True)
    receiver=models.CharField(max_length=30,null=True,blank=True)
    def __str__(self):
        return self.msg
class Request(models.Model):
    sender=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    receiver=models.CharField(max_length=30,null=True,blank=True)
    
    def __str__(self):
        return (f"{self.sender.username} to {self.receiver}")

class Freinds(models.Model):
    sender=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    receiver=models.CharField(max_length=30,null=True,blank=True)
    
    def __str__(self):
        return (f"{self.sender.username} to {self.receiver}")
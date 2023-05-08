from django.db import models

# Create your models here


class User(models.Model):
    username = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=True) 
    phone = models.CharField(max_length=15, null=True)
    city = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.username

class Driver(models.Model):
    unique_id = models.CharField(max_length=100, null=True)
    dname = models.CharField(max_length=100, null=True) 
    dphone = models.CharField(max_length=15, null=True)
    #booking_id = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.unique_id

    

class React(models.Model):
	name = models.CharField(max_length=30)
	detail = models.CharField(max_length=500)
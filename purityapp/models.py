from django.db import models


# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=70)
    password = models.CharField(max_length=70)

    def __str__(self):
        return self.firstname + " " + self.lastname

class Products(models.Model):
    name = models.CharField(max_length=70)
    price = models.IntegerField(default=0)
    description = models.TextField()
    origin = models.CharField(max_length=70, default="Kenya")
    color = models.CharField(max_length=70, default="white")

    def __str__(self):
        return self.name

class Appointment(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    phone = models.IntegerField(default=0)
    date = models.DateTimeField()
    department = models.CharField(max_length=70)
    doctor = models.CharField(max_length=70)
    message = models.TextField()

    def __str__(self):
        return self.name

class Ordered(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    delivery_date = models.DateTimeField()

    def __str__(self):
        return self.name

class ImageModel(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=70)
    price = models.CharField(max_length=70)

    def __str__(self):
        return self.title





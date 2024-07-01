from django.db import models


# Create your models here.

class Vehicle(models.Model):
    title=models.CharField(max_length=100)
    price=models.IntegerField()
    image=models.ImageField(upload_to='vehicle_img')
    options=(
        ('Car','Car'),
        ('Bike','Bike')
    )
    category=models.CharField(max_length=100,choices=options)
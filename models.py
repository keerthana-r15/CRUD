from django.db import models
import datetime

class Customers(models.Model):
    name = models.CharField(max_length=30)
    address = models.TextField(max_length=1000)
    age = models.IntegerField()
    mobile= models.CharField(max_length = 60)
    gender = models.CharField(max_length=10)
    location = models.CharField(max_length=20)
    chennai= models.BooleanField(default=False)
    bangalore = models.BooleanField(default=False)
    delhi = models.BooleanField(default=False)
    jaipur = models.BooleanField(default=False)
    dob = models.DateField(default=datetime.date.today)
    covid = models.BooleanField()
    pic = models.ImageField(null=True, blank=True, upload_to="images/")
    budget = models.FloatField()
   

    class Meta:
        db_table = 'customer_table'

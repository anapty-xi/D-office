from django.db import models
from django.contrib.auth.models import User

class maps(models.Model):
    name = models.CharField(max_length=100)
    scheme = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

class workpalce(models.Model):
    workpalce_code = models.CharField(max_length=10)
    equipment = models.TextField()
    map_id = models.ForeignKey(maps, on_delete=models.CASCADE, related_name='workplace_map')

class booking(models.Model):
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking_workplace')
    workpalce_id = models.ForeignKey(workpalce, on_delete=models.CASCADE, related_name='booked_workplace')
    date = models.DateField(auto_now=True)



from django.db import models
from django.contrib.auth.models import User

class maps(models.Model):
    name = models.CharField(max_length=100)
    scheme = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.name



class workplace(models.Model):
    workplace_code = models.CharField(max_length=10)
    equipment = models.TextField()
    map_id = models.ForeignKey(maps, on_delete=models.CASCADE, related_name='workplace_map')

    def __str__(self):
        return self.workplace_code



class booking(models.Model):
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking_workplace')
    workplace_id = models.ForeignKey(workplace, on_delete=models.CASCADE, related_name='booked_workplace')
    date = models.DateField()

    def __str__(self):
        return f'{self.owner_id} booked {self.workplace_id} for {self.date}'
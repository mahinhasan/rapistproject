from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse
# Create your models here.

choices = [
    ('In jail','In jail'),('Police custady','police custady'),('escaping','escaping')
]

class Rapiest(models.Model):
    name = models.CharField(max_length = 255)
    image = models.ImageField(null = True,blank = True,upload_to='images/')
    incident_date = models.DateTimeField( auto_now=False, auto_now_add=False)
    village = models.CharField(max_length = 100)
    district = models.CharField(max_length=100)
    author = models.ForeignKey(User,default='',  on_delete=models.CASCADE)
    victim = models.CharField(max_length = 255)
    punishment = models.CharField(max_length = 400)
    details = models.TextField()
    status = models.CharField(max_length = 255,choices=choices,default=1)
    views  = models.IntegerField(default=0)
    def __str__(self):
        return self.name+' | '+self.victim   

    def get_absolute_url(self):
        return reverse("rapist-detail", args = str(self.id))
    


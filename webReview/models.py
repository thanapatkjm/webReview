from django.db import models

class Restaurant(models.Model):
    name = models.TextField()
    description = models.TextField()
    address = models.TextField()
    phone_num = models.TextField()
    Category = models.TextField()
    rating = models.FloatField()

class Reviews(models.Model):
    name = models.TextField()
    comment = models.TextField()
    rating = models.FloatField()
    restau = models.ForeignKey(Restaurant,on_delete=models.CASCADE)

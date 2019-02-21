from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Restaurant(models.Model):
    name = models.TextField()
    description = models.TextField()
    address = models.TextField()
    phone_num = models.TextField()
    Category = models.TextField()
    rating = models.FloatField(default = 0)

class Reviews(models.Model):
    name = models.TextField()
    comment = models.TextField()
    rating = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(5.0)],)
    restau = models.ForeignKey(Restaurant,on_delete=models.CASCADE)

# class
# class Category(models.Model):
#     name = models.TextField()
#

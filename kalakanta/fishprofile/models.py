from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Fish(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    species = models.CharField(max_length=100)
    catch_date = models.DateField()
    catch_time = models.TimeField()
    form_of_fishing = models.CharField(max_length=30)
    catch_latitude = models.DecimalField(max_digits=7, decimal_places=5)
    catch_longitude = models.DecimalField(max_digits=8, decimal_places=5)

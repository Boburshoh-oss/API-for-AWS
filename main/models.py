from django.db import models

# Create your models here.

class Customer(models.Model):
    full_name = models.CharField(max_length=250)
    birth_data = models.DateField()
    phone_data = models.CharField(max_length=13)

    def __str__(self):
        
        return self.full_name

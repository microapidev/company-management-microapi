from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phoneNumber = models.IntegerField()
    poBox = models.IntegerField()

    def __str__(self):
        return self.name
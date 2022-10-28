from django.db import models
from user_app.models import MedUser
# Create your models here.



class DrugGroup(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name

class DrugManufacturer(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name

class DrugName(models.Model):
    name = models.CharField(max_length=64, unique=True)
    pharmgroup = models.ForeignKey(DrugGroup, on_delete=models.CASCADE, null=True)
    manufacturer = models.ForeignKey(DrugManufacturer, on_delete=models.CASCADE, null=True)
    form = models.TextField(blank=True)
    indications = models.TextField(blank=True)
    more = models.TextField(blank=True)
    def __str__(self):
        return self.name

class Contacts(models.Model):
    name = models.CharField(max_length=64, unique=False)
    email = models.EmailField(max_length=64, unique=False)
    message = models.TextField(blank=True)
    user = models.ForeignKey(MedUser, on_delete = models.CASCADE)
from django.db import models

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
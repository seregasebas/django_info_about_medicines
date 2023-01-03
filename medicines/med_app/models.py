from django.db import models
from user_app.models import MedUser
# Create your models here.

class ActiveManager(models.Manager):

    def get_queryset(self):
        all_objects = super().get_queryset()
        return all_objects.filter(is_active = True)

class IsActiveMixin(models.Model):
    objects = models.Manager()
    active_objects = ActiveManager()
    is_active = models.BooleanField(default = True, blank=True)

    class Meta:
        abstract = True

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

class Contacts(IsActiveMixin, models.Model):
    name = models.CharField(max_length=64, unique=False)
    email = models.EmailField(max_length=64, unique=False)
    message = models.TextField(blank=True)
    user = models.ForeignKey(MedUser, on_delete = models.CASCADE)

    def is_name(self):
        return self.name is None
    
    def is_email(self):
        return self.email is None

    def is_message(self):
        return self.message is None

    def hello_contacts(self):
        return 'Hello, programmer!'

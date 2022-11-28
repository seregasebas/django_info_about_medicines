from django.db import models
from django.contrib.auth.models import AbstractUser

# # Для сигналов
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# Create your models here.

class MedUser(AbstractUser):
    email = models.EmailField(unique = True)
    is_author = models.BooleanField(default = True)

    # Переопределение метода save
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Создаем профиль
        # Если провиль не создан
        if not Profile.objects.filter(user=self).exists():
            Profile.objects.create(user=self)

class Profile(models.Model):
    # При создании пользователя создать Profile
    info = models.TextField(blank=True)
    user = models.OneToOneField(MedUser, on_delete=models.CASCADE)

# # Сигналы
# @receiver(post_save, sender=MedUser)
# def create_profile(sender, instance, **kwargs):
#     print('Сработал обработчик сигнала')
#     if not Profile.objects.filter(user=instance).exists():
#         Profile.objects.create(user=instance)

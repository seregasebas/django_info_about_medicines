from django.core.management.base import BaseCommand
from med_app.models import Contacts
from mixer.backend.django import mixer

# через терминал скрипт автоматического создания постов
class Command(BaseCommand):

    def handle(self, *args, **options):
        Contacts.objects.all().delete()
        count = 200
        for i in range(count):
            mixer.blend(Contacts)
            print(f'{i} - {(i/count)*100}%')
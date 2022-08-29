from django.core.management.base import BaseCommand
from med_app.models import DrugName, DrugGroup, DrugManufacturer
from .functions import a

# from blogapp.models import Poll

class Command(BaseCommand):

    def handle(self, *args, **options):
        # Выбираем ВСЕ категории
        print('fill_db', a)
        # categories = Category.objects.all()
        # print(categories)
        # print(type(categories))
        # for item in categories:
        #     print(item)
        #     print(item.name)
        #     print(type(item))
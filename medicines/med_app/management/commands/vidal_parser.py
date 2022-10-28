from django.core.management.base import BaseCommand
from med_app.models import DrugName, DrugGroup, DrugManufacturer

from med_app.management.commands.functions import *
import os.path
import json

# from blogapp.models import Poll

class Command(BaseCommand):

    def handle(self, name, *args, **options):
        print('Vidal_parser')
        #Проверяем, что файл с именамни и ссылками есть в директории
        #если нет, то делаем полный парсинг... да, долго, но что поделаешь один раз нужно будет подождать
        if os.path.isfile('name_url.json'):
            #сохраняем данные название препарата - url в переменную
            with open('name_url.json', 'r', encoding = 'utf-8') as new:
                name_url_drug = json.load(new)
        else:
            parser_first()

        # # User вводит название препарата
        # user_input = input('введите название препарата на русском языке: ').lower()
        user_input = name.lower()
        #сохраняем первую букву
        letter = user_input[0].lower()

        #проверяем, что препарат есть в списке 
        if user_input in name_url_drug:
            #проверяем препарат в базе. Если есть, то вытаскиваем инфу оттуда
            if bool(DrugName.objects.filter(name=user_input)):
                #информация об искомом перпарате из своей базы данных
                res_parsing_dict = look_at_my_data(user_input)
                save_file(res_parsing_dict)
                print(f'Информация по преапарату {user_input} есть в базе')
            else:
                res_parsing_dict = res_parsing(user_input, name_url_drug)
                save_file(res_parsing_dict)
                #добавляем в базу данных
                data_to_the_database()
                print(f'Информация по препарату {user_input} добавлена в базу')
        #если нет в списке, то проводим отедльный парсинг с сайта vidal.ru
        else:
            #получаем url_name препарата
            url_name = word_parser(letter)
            #получаем name_url словарь
            name_url_drug = name_url_dict(url_name)
            #результат парсинга и на выходе информация об искомом перпарате
            res_parsing_dict = res_parsing(user_input, name_url_drug)
            #запись данных в файл
            save_file(res_parsing_dict)
            #добавляем в базу данных
            data_to_the_database()

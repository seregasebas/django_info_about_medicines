from unicodedata import name
from django import forms
from .models import Contacts

# class ContactForm(forms.Form):
#     name = forms.CharField(label = 'Имя')
#     email = forms.EmailField(label = 'email')
#     message = forms.CharField(label = 'Сообщение')

class ContactForm(forms.ModelForm):
    name = forms.CharField(label = 'Ваше Имя', widget=forms.TextInput(attrs={'placeholder':'Your Name'}))
    class Meta():
        model = Contacts
        #Вывести все строки
        fields = '__all__'
        # #если нужно ввести не все строки
        # fields = ('name', 'comments')
        # #Либо так можно ввыести не все строки через исключение
        # exclude = ('user',)

class FindForm(forms.Form):
    name = forms.CharField(label = 'Поиск', help_text='введите название препарата на русском языке')

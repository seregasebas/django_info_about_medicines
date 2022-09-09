from unicodedata import name
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label = 'Имя')
    email = forms.EmailField(label = 'email')
    message = forms.CharField(label = 'Сообщение')

class FindForm(forms.Form):
    name = forms.CharField(label = 'Поиск', help_text='введите название препарата на русском языке')

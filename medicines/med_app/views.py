from audioop import reverse
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .forms import ContactForm, FindForm
from django.core.mail import send_mail
# Create your views here.

def main_view(request):
    return render(request, 'med_app/index.html', context = {})

def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            #Получаем данные из формы
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
            f'Комментарий от {name}',
            f'Ваше сообщение {message} принято',
            'from@example.com',
            [email],
            fail_silently=True,
            )
            return render(request, 'med_app/thanks.html', context = {'form':form})
            # return HttpResponseRedirect(reverse('medicines:thanks'))
        else:
            return render(request, 'med_app/contact.html', context = {'form':form})
    else:
        form = ContactForm()
        return render(request, 'med_app/contact.html', context = {'form':form})

def find_drug(request):
    if request.method == 'POST':
        form = FindForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            return render(request, 'med_app/result.html', context = {'form':form})
        else:
            return render(request, 'med_app/find_drug.html', context = {'form':form})
    else:
        form = FindForm()
        return render(request, 'med_app/find_drug.html', context={'form':form})

def thanks(request):
    return render(request, 'med_app/thanks.html', context = {})

def result(request):
    #TODO: Внести код vidal_parser.py
    # принимает ввод со страницы find_drug и возвращает результат
    # результат возращать в виде текста на странице
    return render(request, 'med_app/result.html', context = {})
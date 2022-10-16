from audioop import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import json

from django.urls import reverse_lazy
from .models import DrugName, Contacts
from .forms import ContactForm, FindForm
from django.core.mail import send_mail
from .management.commands import functions, vidal_parser
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import ContextMixin

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required
# Create your views here.

def main_view(request):
    return render(request, 'med_app/index.html', context = {})

# Только залогиненные пользоватеи могут оставить комментарий
@login_required
# def contacts(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST, files=request.FILES)
#         if form.is_valid():
#             #Получаем данные из формы
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
#             send_mail(
#             f'Комментарий от {name}',
#             f'Ваше сообщение {message} принято',
#             'from@example.com',
#             [email],
#             fail_silently=True,
#             )
#             functions.contact_to_the_database(name, email, message)
            
#             #TODO:Добавить в форму текущего пользователя
#             form.instance = request.user
#             form.save
#             return HttpResponseRedirect(reverse('med_app:thanks'))
#         else:
#             return render(request, 'med_app/contact.html', context = {'form':form})
#     else:
#         form = ContactForm()
#         return render(request, 'med_app/contact.html', context = {'form':form})

def find_drug(request):
    if request.method == 'POST':
        form = FindForm(request.POST)
        if form.is_valid():
            #Получаем данные из формы
            name = form.cleaned_data['name']
            # Объект класса Command из парсинга видаля
            res = vidal_parser.Command()
            # Метод объекта класса для парсинга
            res.handle(name)
            view_info = functions.look_at_my_data(name)
            return render(request, 'med_app/result.html', context = {'view_info':view_info})
        else:
            return render(request, 'med_app/find_drug.html', context = {'form':form})
    else:
        form = FindForm()
        return render(request, 'med_app/find_drug.html', context={'form':form})

def thanks(request):
    return render(request, 'med_app/thanks.html', context = {})

# Mixin для множественного наследования
class NameContextMixin(ContextMixin):
    #передаем название контекста
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['name'] = 'Комментарии'
        return context

#CRUD (create, read, update, delete)

class CommentsViews(ListView, NameContextMixin):
    model = Contacts
    template_name = 'med_app/comments_view.html'

    #получение данных
    def get_queryset(self):
        return Contacts.objects.all()

class CommentsDetail(DetailView, NameContextMixin):
    model = Contacts
    template_name = 'med_app/comments_detail.html'

    #Метод получения get запроса
    def get(self, request, *args, **kwargs):

        self.comment_id = kwargs['pk']
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return get_object_or_404(Contacts, pk = self.comment_id)

# LoginRequiredMixin - должен идти первым. Право писать комменты только у залогиненных
class CommentsCreate(LoginRequiredMixin, CreateView, NameContextMixin):
    model = Contacts
    fields = ('name', 'email', 'message') #'__all__'  
    success_url = reverse_lazy('med_app:comments_view')
    template_name = 'med_app/comments_create.html'

    #когда пришел post запрос
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    #метод срабатывает после того как форма валидна
    def form_valid(self, form):

        form.instance.user = self.request.user
        return super().form_valid(form)

class CommentsUpdate(LoginRequiredMixin, UpdateView):
    model = Contacts
    fields = ('name', 'email', 'message')
    success_url = reverse_lazy('med_app:comments_view')
    template_name = 'med_app/comments_create.html'

class CommentsDelete(DeleteView):
    model = Contacts
    template_name = 'med_app/comments_delete.html'
    success_url = reverse_lazy('med_app:comments_view')
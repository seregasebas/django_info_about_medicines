from django.urls import path
from med_app import views

app_name = 'med_app'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('contact/', views.contacts, name='contact'),
    path('find_drug/', views.find_drug, name='find_drug'),
    path('thanks/', views.thanks, name='thanks'),
]
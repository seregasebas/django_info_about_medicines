from django.urls import path, include
from .models import Contacts, DrugName, DrugGroup
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class ContactsSerializer(serializers.HyperlinkedModelSerializer):
    # чтобы работали связки
    user = serializers.SlugRelatedField(read_only=True, slug_field='is_author')

    class Meta:
        model = Contacts
        fields = '__all__' #['name', 'email', 'message']


class DrugSerializer(serializers.HyperlinkedModelSerializer):
    # чтобы работали связки
    pharmgroup = serializers.SlugRelatedField(read_only=True, slug_field='name')
    manufacturer = serializers.SlugRelatedField(read_only=True, slug_field='name')
    
    class Meta:
        model = DrugName
        fields = '__all__' #['name', 'form', 'indications', 'more']

class DrugGroupSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = DrugGroup
        fields = '__all__' 


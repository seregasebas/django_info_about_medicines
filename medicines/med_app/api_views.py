from .models import Contacts, DrugName
from .serialization import ContactsSerializer, DrugSerializer
from rest_framework import viewsets


# ViewSets define the view behavior.
class ContactsViewSet(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer

# ViewSets define the view behavior.
class DrugNameViewSet(viewsets.ModelViewSet):
    queryset = DrugName.objects.all()
    serializer_class = DrugSerializer
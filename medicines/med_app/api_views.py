from .models import Contacts, DrugName, DrugGroup
from .serialization import ContactsSerializer, DrugSerializer, DrugGroupSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .permissions import ReadOnly, IsAuthor
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

# ViewSets define the view behavior.
class ContactsViewSet(viewsets.ModelViewSet):
    # права доступа для редактирования только у автора, смотреть могут все 
    permission_classes = [IsAdminUser|IsAuthor|ReadOnly]
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer

# ViewSets define the view behavior.
class DrugNameViewSet(viewsets.ModelViewSet):
    # права доступа для редактирования только у админа, смотреть могут все
    permission_classes = [IsAdminUser|ReadOnly]
    queryset = DrugName.objects.all()
    serializer_class = DrugSerializer

# ViewSets define the view behavior.
class DrugGroupViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = DrugGroup.objects.all()
    serializer_class = DrugGroupSerializer
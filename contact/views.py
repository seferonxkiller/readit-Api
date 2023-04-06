from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializer


class ContactListCreateApiView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

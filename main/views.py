from rest_framework import serializers, viewsets

from main.serializers import CustomerSerializers
from .models import Customer
# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers

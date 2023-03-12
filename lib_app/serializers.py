from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from django.core import validators
from django.db.models import Q

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

class PurchasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchases
        fields = "__all__"

class RentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rents
        fields = "__all__"
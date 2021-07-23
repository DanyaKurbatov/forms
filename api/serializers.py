from rest_framework import serializers
from phonenumber_field.modelfields import PhoneNumberField


class FormSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=64)
    email = serializers.EmailField(max_length=254)
    phone = PhoneNumberField()
    date = serializers.DateField()
    text = serializers.CharField()


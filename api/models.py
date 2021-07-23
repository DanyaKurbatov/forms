from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Form(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=254)
    phone = PhoneNumberField()
    date = models.DateField()
    text = models.TextField()

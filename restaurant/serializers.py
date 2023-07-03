from rest_framework.serializers import ModelSerializer
from .models import Booking
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    # Serializer fields and configurations
    class Meta:
        model = User
        fields = '__all__'



class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

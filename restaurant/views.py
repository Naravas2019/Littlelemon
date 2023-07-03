from rest_framework.viewsets import ModelViewSet
from .models import Booking
from .serializers import BookingSerializer
from django.http import HttpResponse
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .serializers import UserSerializer



def index(request):
    return HttpResponse("Hello, World!")


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated] 
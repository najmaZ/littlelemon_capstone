from rest_framework.decorators import permission_classes
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Booking, Menu,MenuItem
from .serializers import MenuSerializer, BookingSerializer , MenuItemSerializer
from django.shortcuts import render

# Create your views here.
def index(request):
     return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


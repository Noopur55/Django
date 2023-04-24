from opinio_ate.models import Restaurant,Dish
from rest_framework import viewsets
from opinio_ate.serializers import RestaurantSerializer,DishSerializer
# Create your views here.

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset=Restaurant.objects.all()
    serializer_class=RestaurantSerializer
    
class DishViewSet(viewsets.ModelViewSet):
    queryset=Dish.objects.all()
    serializer_class=DishSerializer

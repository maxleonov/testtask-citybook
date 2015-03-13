from rest_framework import viewsets
from citybook.models import City
from citybook.serializers import CitySerializer


class CityViewSet(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()
    model = City


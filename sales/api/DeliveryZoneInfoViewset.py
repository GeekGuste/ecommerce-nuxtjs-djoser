from rest_framework.viewsets import ModelViewSet
from sales.serializers import DeliveryZoneInfoSerializer

class DeliveryZoneInfoViewset(ModelViewSet):
    serializer_class = DeliveryZoneInfoSerializer

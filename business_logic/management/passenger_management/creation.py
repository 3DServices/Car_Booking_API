from core.management.creation import Creator
from authentication.models import Courier

class CourierCreator(Creator):
    
    def  create(self, validated_data: dict) -> object:
        user = validated_data.get('user')
        courier = Courier.objects.create(user=user)
        return courier

from core.management.deletion import Deleter
from authentication.models import Courier

class CourierDeleter(Deleter):
    
    def delete(self, instance_id):
        return Courier.objects.delete(id=instance_id)

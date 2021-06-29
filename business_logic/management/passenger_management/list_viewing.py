from core.management.list_viewing import ListViewer
from authentication.models import Courier

class CourierListViewer(ListViewer):
    
    def get_list(self):
        return Courier.objects.all()

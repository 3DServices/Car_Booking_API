from core.management.retrieval import Retriever
from authentication.models import Courier


class CourierRetriever(Retriever):

    def retrieve(self, instance_id) -> object:
        instance = Courier.objects.get(id=instance_id)
        return instance

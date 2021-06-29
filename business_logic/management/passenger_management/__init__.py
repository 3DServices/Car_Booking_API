from core.management import AbstractManager

from .creation import CourierCreator as Creator
from .list_viewing import CourierListViewer as ListViewer
from  .retrieval import CourierRetriever as Retriever
from .updating import CourierUpdater as Updater
from .patching import CourierPatcher as Patcher
from .deletion import CourierDeleter as Deleter

class CourierManager(AbstractManager):

    def __init__(self) -> None:
        super().__init__()
        self.set_creator(Creator())
        self.set_list_viewer(ListViewer())
        self.set_retriever(Retriever())
        self.set_updater(Updater())
        self.set_patcher(Patcher())
        self.set_deleter(Deleter())

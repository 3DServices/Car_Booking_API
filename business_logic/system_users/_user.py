from abc import ABC as AbstractClass

from business_logic.user_accounts import UserAccountsController


class AbstractUser(AbstractClass):
    """
    A controller for the system user.
    """
    # _profile_controller: None
    _accounts_controller: None
    # _organizations_controller: None
    # _orders_controller: None
    # _payments_controller: None

    # # Mutators
    # def set_profile_controller(self, profile_controller):
    #     self._profile_controller = profile_controller

    def set_accounts_controller(self, accounts_controller):
        self._accounts_controller = accounts_controller

    # def set_organizations_controller(self, organizations_controller):
    #     self._organizations_controller = organizations_controller

    # def set_orders_controller(self, orders_controller):
    #     self._orders_controller = orders_controller

    # def set_payments_controller(self, payments_controller):
    #     self._payments_controller = payments_controller

    # # Accessors
    # def get_profile_controller(self):
    #     return self._profile_controller

    def get_accounts_controller(self):
        return self._accounts_controller


class User(AbstractUser):
    # Generic User Operations
    def register_user(self, request):
        self.set_accounts_controller(UserAccountsController())
        return self.get_accounts_controller().register_user(request)

    def register_passenger(self, request):
        self.set_accounts_controller(UserAccountsController())
        return self.get_accounts_controller().register_passenger(request)

    def register_driver(self, request):
        self.set_accounts_controller(UserAccountsController())
        return self.get_accounts_controller().register_driver(request)

    def register_fleetmanager(self, request):
        self.set_accounts_controller(UserAccountsController())
        return self.get_accounts_controller().register_fleetmanager(request)

    def register_systemadmin(self, request):
        self.set_accounts_controller(UserAccountsController())
        return self.get_accounts_controller().register_systemadmin(request)

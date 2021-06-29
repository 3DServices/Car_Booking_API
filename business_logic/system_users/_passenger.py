from . import _user
User = _user.User


class Passenger(User):
    """
    A controller for Passenger as a system user.
    """

    def __init__(self,):
        super()

    # Mutators

    # Accessors

    # Generic User Operations
    def register_passenger(self, validated_data):
        return self.get_accounts_controller().register_passenger(validated_data)

from . import _user
User = _user.User


class Driver(User):
    """
    A controller for Driver as a system user.
    """

    def __init__(self,):
        super()

    # Mutators

    # Accessors

    # Generic User Operations
    def register_driver(self, validated_data):
        return self.get_accounts_controller().register_driver(validated_data)

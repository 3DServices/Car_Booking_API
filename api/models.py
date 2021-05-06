from django.db import models
from .mixins.django_default_user_mixin import DefaultUser
import uuid

class User(DefaultUser):
    """

    """
    id = models.Charfield(primary_key= True, max_length = 50, default=uuid.uuid4())

class SystemAdmin(models.Model):
    """

    """
    id = models.Charfield(primary_key=True, max_length=50, default=uuid.uuid4())
    user = models.OneToOneField(User, related_name="SysAdmin", on_delete= models.CASCADE)


class FleetManager(models.Model):
    """

    """
    id = models.Charfield(primary_key=True, max_length=50, default=uuid.uuid4())
    user = models.OneToOneField(User, related_name="FleetManager", on_delete=models.CASCADE)


class Passenger(models.Model):
    """

    """
    id = models.Charfield(primary_key=True, max_length=50, default=uuid.uuid4())
    user = models.OneToOneField(User, related_name="Passenger", on_delete=models.CASCADE)


class Driver(models.Model):
    """

    """
    id = models.Charfield(primary_key=True, max_length=50, default=uuid.uuid4())
    user = models.OneToOneField(User, related_name="Driver", on_delete=models.CASCADE)




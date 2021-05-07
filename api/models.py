from django.db import models

from .mixins.django_default_user_mixin import DefaultUser
import uuid


class User(DefaultUser):
    """

    """
    Id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())

    def __str__(self):
        return self.Id


class SystemAdmin(models.Model):
    """

    """
    Id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())
    user = models.OneToOneField(
        User, related_name="SysAdmin", on_delete=models.CASCADE)


class FleetManager(models.Model):
    """

    """
    Id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())
    user = models.OneToOneField(
        User, related_name="FleetManager", on_delete=models.CASCADE)


class Passenger(models.Model):
    """

    """
    Id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())
    user = models.OneToOneField(
        User, related_name="Passenger", on_delete=models.CASCADE)


class Driver(models.Model):
    """

    """
    Id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())
    user = models.OneToOneField(
        User, related_name="Driver", on_delete=models.CASCADE)

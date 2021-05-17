from django.db import models

from .mixins.django_default_user_mixin import DefaultUser
from api.mixins.base_model_mixin import BaseModel
import uuid
from phonenumber_field.modelfields import PhoneNumberField


class User(DefaultUser):
    """

    """
    Id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())
    primary_contact = PhoneNumberField(default='+256777777777')
    secondary_contact = PhoneNumberField(default='+256777777777')
    # profile_photo =

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.Id = uuid.uuid4()
        super(User, self).save()

    def __str__(self):
        _str = '%s' % self.first_name
        return _str

    """
    specifying the meta data
        class Meta:
        verbose_name_plural = "Categories"
        ordering = ['first_name]
    """


class SystemAdmin(models.Model):
    """

    """
    id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())
    user = models.OneToOneField(
        User, related_name="SysAdmin", on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(SystemAdmin, self).save()

    def __str__(self):
        _str = '%s' % self.user.first_name
        return _str


class FleetManager(models.Model):
    """

    """
    id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())
    user = models.OneToOneField(
        User, related_name="FleetManager", on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(FleetManager, self).save()

    def __str__(self):
        _str = '%s' % self.user.first_name
        return _str


class Passenger(models.Model):
    """

    """
    id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())
    user = models.OneToOneField(
        User, related_name="Passenger", on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(Passenger, self).save()

    def __str__(self):
        _str = '%s' % self.user.first_name
        return _str


class Driver(models.Model):
    """

    """
    id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())
    permit = models.CharField(max_length=50,
                              default='UAX')
    user = models.OneToOneField(
        User, related_name="Driver", on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(Driver, self).save()

    def __str__(self):
        _str = '%s' % self.user.first_name
        return _str

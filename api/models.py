from django.db import models
from .mixins.django_default_user_mixin import DefaultUser
import uuid


class User(DefaultUser):
    """

    """
    id = models.Charfield(primary_key=True, max_length=50, default=uuid.uuid4())

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
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
    id = models.CharField(primary_key=True, max_length=50, default=uuid.uuid4())
    user = models.OneToOneField(User, related_name="SysAdmin", on_delete=models.CASCADE)

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
    id = models.CharField(primary_key=True, max_length=50, default=uuid.uuid4())
    user = models.OneToOneField(User, related_name="FleetManager", on_delete=models.CASCADE)

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
    id = models.CharField(primary_key=True, max_length=50, default=uuid.uuid4())
    user = models.OneToOneField(User, related_name="Passenger", on_delete=models.CASCADE)

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
    id = models.CharField(primary_key=True, max_length=50, default=uuid.uuid4())
    user = models.OneToOneField(User, related_name="Driver", on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(Driver, self).save()

    def __str__(self):
        _str = '%s' % self.user.first_name
        return _str

class Organisation(BaseModel):
    id = models.CharField(primary_key = True, max_length = 50, default = uuid.uuid4())
    name = models.CharField(primary_key = True, max_length = 50, default = 'organisationx')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(Organisation, self).save()

    def __str__(self):
        _str = '%s' % self.name
        return _str

class OrganisationFleetManager(BaseModel):
    id = models.CharField(primary_key=True, max_length=50, default = uuid.uuid4())
    organisation = models.OneToManyField(Organisation, related_name="organisations", on_delete=models.CASCADE)
    fleet_manager = models.OneToManyField(FleetManager, related_name="fleet_managers", on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(OrganisationFleetManager, self).save()

    def __str__(self):
        _str = '%s %s' % self.organisation.name,self.fleet_manager.user.firstname
        return _str


class OrganisationDriver(BaseModel):
    id = models.CharField(primary_key=True, max_length=50, default = uuid.uuid4())
    organisation = models.OneToManyField(Organisation, related_name="Organisation", on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(OrganisationDriver, self).save()

    def __str__(self):
        _str = '%s' % self.user.first_name
        return _str

class OrganisationVehicle(BaseModel):
    id = models.CharField(primary_key=True, max_length=50, default = uuid.uuid4())
    organisation = models.OneToManyField(Organisation, related_name="Organisation", on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(User, self).save()

    def __str__(self):
        _str = '%s' % self.user.first_name
        return _str

class Project(BaseModel):
    id = models.CharField(primary_key=True, max_length=50, default = uuid.uuid4())
    organisation = models.OneToManyField(Organisation, related_name="Organisation", on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(User, self).save()

    def __str__(self):
        _str = '%s' % self.first_name
        return _str

class Branch(BaseModel):
    id = models.CharField(primary_key=True, max_length=50, default = uuid.uuid4())
    organisation = models.OneToManyField(Organisation, related_name="Organisation", on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(User, self).save()

    def __str__(self):
        _str = '%s' % self.first_name
        return _str


class Station(BaseModel):
    id = models.CharField(primary_key=True, max_length=50, default = uuid.uuid4())
    organisation = models.OneToManyField(Organisation, related_name="Organisation", on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(User, self).save()

    def __str__(self):
        _str = '%s' % self.first_name
        return _str

class Department(BaseModel):
    id = models.CharField(primary_key=True, max_length=50, default = uuid.uuid4())
    organisation = models.OneToManyField(Organisation, related_name="Organisation", on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(User, self).save()

    def __str__(self):
        _str = '%s' % self.first_name
        return _str


class Directorate(BaseModel):
    id = models.CharField(primary_key=True, max_length=50, default = uuid.uuid4())
    organisation = models.OneToManyField(Organisation, related_name="Organisation", on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(User, self).save()

    def __str__(self):
        _str = '%s' % self.first_name
        return _str

class Blacklist(BaseModel):
    id = models.CharField(primary_key=True, max_length=50, default=uuid.uuid4())
    organisation = models.OneToManyField(Organisation, related_name="Organisation", on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(User, self).save()

    def __str__(self):
        _str = '%s' % self.first_name
        return _str

class PassengerBlacklist(BaseModel):
    id = models.CharField(primary_key=True, max_length=50, default=uuid.uuid4())
    blacklist = models.OneToManyField(Blacklist, related_name="Blacklist", on_delete=models.CASCADE)
    reason = models.CharField(max_length = 100)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(User, self).save()

    def __str__(self):
        _str = '%s' % self.first_name
        return _str


class DriverBlacklist(BaseModel):
    id = models.CharField(primary_key=True, max_length=50, default=uuid.uuid4())
    blacklist = models.OneToManyField(Blacklist, related_name="Blacklist", on_delete=models.CASCADE)
    reason = models.CharField(max_length=100)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(User, self).save()

    def __str__(self):
        _str = '%s' % self.first_name
        return _str

class VehicleBlacklist(BaseModel):
    id = models.CharField(primary_key=True, max_length=50, default=uuid.uuid4())
    blacklist = models.OneToManyField(Blacklist, related_name="Blacklist", on_delete=models.CASCADE)
    reason = models.CharField(max_length = 100)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(User, self).save()

    def __str__(self):
        _str = '%s' % self.first_name
        return _str
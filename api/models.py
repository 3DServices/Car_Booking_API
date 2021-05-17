from django.db import models

from .mixins.django_default_user_mixin import DefaultUser
from .mixins.base_model_mixin import BaseModel
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
    Id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())
    user = models.OneToOneField(
        User, related_name="SysAdmin", on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.Id = uuid.uuid4()
        super(SystemAdmin, self).save()

    def __str__(self):
        _str = '%s' % self.user.first_name
        return _str


class FleetManager(models.Model):
    """

    """
    Id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())
    user = models.OneToOneField(
        User, related_name="FleetManager", on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.Id = uuid.uuid4()
        super(FleetManager, self).save()

    def __str__(self):
        _str = '%s' % self.user.first_name
        return _str


class Passenger(models.Model):
    """

    """
    Id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())
    user = models.OneToOneField(
        User, related_name="Passenger", on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.Id = uuid.uuid4()
        super(Passenger, self).save()

    def __str__(self):
        _str = '%s' % self.user.first_name
        return _str


class Driver(models.Model):
    """

    """
    Id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())
    permit = models.CharField(max_length=50,
                              default='UAX')
    user = models.OneToOneField(
        User, related_name="Driver", on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.Id = uuid.uuid4()
        super(Driver, self).save()

    def __str__(self):
        _str = '%s' % self.user.first_name
        return _str


class Vehicle(models.Model):
    """

    """
    Id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())
    type_of_vehicle = models.CharField(max_length=50, default='range_rover')
    brand = models.CharField(max_length=50, default='range_rover')
    carrying_capacity = models.CharField(max_length=50,
                                         default='range_rover')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(Vehicle, self).save()

    def __str__(self):
        _str = '%s' % self.type_of_vehicle
        return _str


class Organisation(BaseModel):
    id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())
    name = models.CharField(
        max_length=50, default='organisationx')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(Organisation, self).save()

    def __str__(self):
        _str = '%s' % self.name
        return _str


class OrganisationFleetManager(BaseModel):
    id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())
    organisation = models.ForeignKey(
        Organisation, related_name="organisations", on_delete=models.CASCADE)
    fleet_manager = models.ForeignKey(
        FleetManager, related_name="fleet_managers", on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(OrganisationFleetManager, self).save()

    def __str__(self):
        _str = '%s %s' % self.organisation.name, self.fleet_manager.user.firstname
        return _str


class OrganisationDriver(BaseModel):
    id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())
    organisation = models.ForeignKey(
        Organisation, related_name="Organisation_driver", on_delete=models.CASCADE)
    driver = models.ForeignKey(
        Driver, related_name="drivers", on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(OrganisationDriver, self).save()

    def __str__(self):
        _str = '%s %s' % self.organisation.name, self.driver.user.firstname
        return _str


class OrganisationVehicle(BaseModel):
    id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())
    organisation = models.ForeignKey(
        Organisation, related_name="Organisation_vehicle", on_delete=models.CASCADE)

    vehicle = models.ForeignKey(
        Vehicle, related_name="vehicles", on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(OrganisationVehicle, self).save()

    def __str__(self):
        _str = '%s %s' % self.organisation.name, self.vehicle.type_of_vehicle
        return _str


class Project(BaseModel):
    id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())
    name = models.CharField(max_length=50, default='projectx')
    organisation = models.ForeignKey(
        Organisation, related_name="Organisations", on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(Project, self).save()

    def __str__(self):
        _str = '%s' % self.name
        return _str


class Branch(BaseModel):
    id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())

    name = models.CharField(max_length=50, default='branchx')

    organisation = models.ForeignKey(
        Organisation, related_name="Branch_organisations", on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(Branch, self).save()

    def __str__(self):
        _str = '%s' % self.name
        return _str

    class Meta:
        verbose_name_plural = "Branches"
        ordering = ['name']


class Station(BaseModel):
    id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())
    name = models.CharField(max_length=50, default='Stationx')
    organisation = models.ForeignKey(
        Organisation, related_name="Station_organisations", on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(Station, self).save()

    def __str__(self):
        _str = '%s' % self.name
        return _str


class Department(BaseModel):
    id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())
    name = models.CharField(max_length=50, default='departmentx')
    organisation = models.ForeignKey(
        Organisation, related_name="Department_organisations", on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(Department, self).save()

    def __str__(self):
        _str = '%s' % self.name
        return _str


class Directorate(BaseModel):
    id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())
    name = models.CharField(max_length=50, default='directoratex')

    organisation = models.ForeignKey(
        Organisation, related_name="Directorate_organisations", on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(Directorate, self).save()

    def __str__(self):
        _str = '%s' % self.name
        return _str


class Blacklist(BaseModel):
    id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())
    organisation = models.ForeignKey(
        Organisation, related_name="Blacklist_organisations", on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(Blacklist, self).save()

    def __str__(self):
        _str = '%s' % self.organisation.name
        return _str


class PassengerBlacklist(BaseModel):
    id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())
    blacklist = models.ForeignKey(
        Blacklist, related_name="Blacklists", on_delete=models.CASCADE)

    passenger = models.ForeignKey(
        Passenger, related_name="Passengers", on_delete=models.CASCADE)
    reason = models.CharField(max_length=100)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(PassengerBlacklist, self).save()

    def __str__(self):
        _str = '%s' % self.passenger.user.first_name
        return _str


class DriverBlacklist(BaseModel):
    id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())
    blacklist = models.ForeignKey(
        Blacklist, related_name="Driver_blacklists", on_delete=models.CASCADE)

    driver = models.ForeignKey(
        Driver, related_name="Drivers", on_delete=models.CASCADE)
    reason = models.CharField(max_length=100)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(DriverBlacklist, self).save()

    def __str__(self):
        _str = '%s' % self.driver.user.first_name
        return _str


class VehicleBlacklist(BaseModel):
    id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())
    blacklist = models.ForeignKey(
        Blacklist, related_name="Vehicle_blacklists", on_delete=models.CASCADE)

    vehicle = models.ForeignKey(
        Vehicle, related_name="Vehicle", on_delete=models.CASCADE)
    reason = models.CharField(max_length=100)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(VehicleBlacklist, self).save()

    def __str__(self):
        _str = '%s' % self.vehicle.type_of_vehicle
        return _str

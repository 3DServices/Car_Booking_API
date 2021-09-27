from django.db import models

from authentication.models import User
from .mixins.base_model_mixin import BaseModel
import uuid
from authentication.models import (Driver, Passenger, FleetManager)
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Vehicle(BaseModel):
    """

    """
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    type_of_vehicle = models.CharField(max_length=50, default='Double Cabin')
    brand = models.CharField(max_length=50, default='Toyota')
    carrying_capacity = models.CharField(max_length=50,
                                         default='4')
    is_available = models.BooleanField(default=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(Vehicle, self).save()

    def __str__(self):
        _str = '%s' % self.type_of_vehicle
        return _str


class Organisation(BaseModel):
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
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
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    organisation = models.ForeignKey(
        Organisation, on_delete=models.CASCADE)
    fleet_manager = models.ForeignKey(
        FleetManager, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(OrganisationFleetManager, self).save()

    def __str__(self):
        _str = '%s %s' % (self.organisation.name,
                          self.fleet_manager.user.first_name)
        return _str


class OrganisationDriver(BaseModel):
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    organisation = models.ForeignKey(
        Organisation, on_delete=models.CASCADE)
    driver = models.ForeignKey(
        Driver, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(OrganisationDriver, self).save()

    def __str__(self):
        _str = '%s %s' % (self.organisation.name, self.driver.user.first_name)
        return _str


class OrganisationPassenger(BaseModel):
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    organisation = models.ForeignKey(
        Organisation, on_delete=models.CASCADE)
    passenger = models.ForeignKey(
        Passenger, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(OrganisationPassenger, self).save()

    def __str__(self):
        _str = '%s %s' % (self.organisation.name,
                          self.passenger.user.first_name)
        return _str


class OrganisationVehicle(BaseModel):
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    organisation = models.ForeignKey(
        Organisation, on_delete=models.CASCADE)

    vehicle = models.ForeignKey(
        Vehicle, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(OrganisationVehicle, self).save()

    def __str__(self):
        _str = '%s %s' % (self.organisation.name, self.vehicle.type_of_vehicle)
        return _str


class Project(BaseModel):
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    name = models.CharField(max_length=50, default='projectx')
    organisation = models.ForeignKey(
        Organisation, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(Project, self).save()

    def __str__(self):
        _str = '%s' % self.name
        return _str


class Region(BaseModel):
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    name = models.CharField(max_length=50, default='projectx')
    organisation = models.ForeignKey(
        Organisation, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(Region, self).save()

    def __str__(self):
        _str = '%s' % self.name
        return _str


class Branch(BaseModel):
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))

    name = models.CharField(max_length=50, default='branchx')

    organisation = models.ForeignKey(
        Organisation, on_delete=models.CASCADE)

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
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    name = models.CharField(max_length=50, default='Stationx')
    organisation = models.ForeignKey(
        Organisation, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(Station, self).save()

    def __str__(self):
        _str = '%s' % self.name
        return _str


class Department(BaseModel):
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    name = models.CharField(max_length=50, default='departmentx')
    organisation = models.ForeignKey(
        Organisation, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(Department, self).save()

    def __str__(self):
        _str = '%s' % self.name
        return _str


class Directorate(BaseModel):
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    name = models.CharField(max_length=50, default='directoratex')

    organisation = models.ForeignKey(
        Organisation, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(Directorate, self).save()

    def __str__(self):
        _str = '%s' % self.name
        return _str


class DirectorateDepartment(BaseModel):
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    directorate = models.ForeignKey(
        Directorate, on_delete=models.CASCADE)

    department = models.ForeignKey(
        Department, on_delete=models.CASCADE)

    name = models.CharField(max_length=50, default='directoratex')

    organisation = models.ForeignKey(
        Organisation, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(DirectorateDepartment, self).save()

    def __str__(self):
        _str = '%s' % self.name
        return _str


class Blacklist(BaseModel):
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    reason = models.CharField(max_length=100, default='not good')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(Blacklist, self).save()

    def __str__(self):
        _str = '%s' % self.organisation.name
        return _str


class PassengerBlacklist(BaseModel):
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    blacklist = models.ForeignKey(
        Blacklist, on_delete=models.CASCADE)

    passenger = models.ForeignKey(
        Passenger, on_delete=models.CASCADE)
    # reason = models.CharField(max_length=100)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(PassengerBlacklist, self).save()

    def __str__(self):
        _str = '%s' % self.passenger.user.first_name
        return _str


class DriverBlacklist(BaseModel):
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    blacklist = models.ForeignKey(
        Blacklist, on_delete=models.CASCADE)

    driver = models.ForeignKey(
        Driver, on_delete=models.CASCADE)
    # reason = models.CharField(max_length=100)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(DriverBlacklist, self).save()

    def __str__(self):
        _str = '%s' % self.driver.user.first_name
        return _str


class VehicleBlacklist(BaseModel):
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    blacklist = models.ForeignKey(
        Blacklist, on_delete=models.CASCADE)

    vehicle = models.ForeignKey(
        Vehicle, on_delete=models.CASCADE)
    # reason = models.CharField(max_length=100)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(VehicleBlacklist, self).save()

    def __str__(self):
        _str = '%s' % self.vehicle.type_of_vehicle
        return _str


class Trip(BaseModel):
    STATUS = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Declined', 'Declined'),
    )
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    pick_up_location = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    destination = models.CharField(max_length=100)
    vehicle = models.ForeignKey(
        Vehicle, on_delete=models.CASCADE)
    reason = models.CharField(max_length=100)
    driver = models.ForeignKey(
        Driver, on_delete=models.CASCADE)

    status = models.CharField(
        max_length=10, null=False, choices=STATUS, default='Pending')
    started_at = models.DateTimeField(blank=True, null=True)
    ended_at = models.DateTimeField(blank=True, null=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(Trip, self).save()

    def __str__(self):
        _str = '%s' % self.id
        return _str


class OrganisationTrip(BaseModel):
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    organisation = models.ForeignKey(
        Organisation, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(OrganisationTrip, self).save()

    def __str__(self):
        _str = '%s' % self.organisation.name
        return _str


class PassengerTrip(BaseModel):
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    passenger = models.ForeignKey(
        Passenger, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(PassengerTrip, self).save()

    def __str__(self):
        _str = '%s' % self.id
        return _str


class OrganisationPassengerTrip(BaseModel):
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    passenger_trip = models.ForeignKey(
        PassengerTrip, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(OrganisationPassengerTrip, self).save()

    def __str__(self):
        _str = '%s' % self.id
        return _str


class DriverTrip(BaseModel):
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(DriverTrip, self).save()

    def __str__(self):
        _str = '%s' % self.id
        return _str


class FleetManagerTrip(BaseModel):
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    pick_up_location = models.CharField(max_length=100)
    date = models.DateField()
    destination = models.CharField(max_length=100)
    vehicle = models.ForeignKey(
        Vehicle, on_delete=models.CASCADE)
    reason = models.CharField(max_length=100)
    passenger = models.ForeignKey(
        Passenger, on_delete=models.CASCADE)
    reason = models.CharField(max_length=100)
    driver = models.ForeignKey(
        Driver, on_delete=models.CASCADE)
    reason = models.CharField(max_length=100)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(FleetManagerTrip, self).save()

    def __str__(self):
        _str = '%s' % self.id
        return _str


class Notification(BaseModel):
    STATUS = (
        ('Sent', 'Sent'),
        ('Not sent', 'Not sent'),
    )
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    expo_token = models.CharField(max_length=100)
    status = models.CharField(
        max_length=10, null=False, choices=STATUS, default='Pending')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(Notification, self).save()

    def __str__(self):
        _str = '%s' % self.id
        return _str


class PassengerNotification(BaseModel):

    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(PassengerNotification, self).save()

    def __str__(self):
        _str = '%s' % self.id
        return _str


class ProjectVehicleDeploy(BaseModel):
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE)

    vehicle = models.ForeignKey(
        Vehicle, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(ProjectVehicleDeploy, self).save()

    def __str__(self):
        _str = '%s' % self.project
        return _str


class StationVehicleDeploy(BaseModel):
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    station = models.ForeignKey(
        Station, on_delete=models.CASCADE)

    vehicle = models.ForeignKey(
        Vehicle, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(StationVehicleDeploy, self).save()

    def __str__(self):
        _str = '%s' % self.station
        return _str


class PhoneNumber(BaseModel):
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    number = PhoneNumberField(max_length=16, unique=True, blank=False)
    user = models.ForeignKey(
        User,  null=False, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(PhoneNumber, self).save()

    def __str__(self):
        _str = '%s' % self.number
        return _str


class UserPhoneNumber (BaseModel):

    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    user = models.ForeignKey(
        User, related_name='phone_numbers', null=False, on_delete=models.CASCADE)
    phone_number = models.ForeignKey(
        PhoneNumber, null=False, on_delete=models.CASCADE)
    primary = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(UserPhoneNumber, self).save()

    def __str__(self):
        _str = '%s' % self.phone_number.number
        return _str


class Rating (BaseModel):

    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    rate_value = models.FloatField(default=0.0, null=False)
    reason = models.CharField(max_length=100)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(Rating, self).save()

    def __str__(self):
        _str = '%s' % self.reason
        return _str


class PassengerRating (BaseModel):

    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    passenger = models.ForeignKey(
        Passenger, on_delete=models.CASCADE)

    rating = models.ForeignKey(
        Rating, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(PassengerRating, self).save()

    def __str__(self):
        _str = '%s' % self.rating.reason
        return _str


class DriverRating (BaseModel):

    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))

    driver = models.ForeignKey(
        Driver, on_delete=models.CASCADE)

    rating = models.ForeignKey(
        Rating, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(DriverRating, self).save()

    def __str__(self):
        _str = '%s' % self.rating.reason
        return _str

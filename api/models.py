from django.db import models

from authentication.models import User
from .mixins.base_model_mixin import BaseModel
import uuid
from authentication.models import (Driver, Passenger, FleetManager)


class Vehicle(BaseModel):
    """

    """
    id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())
    type_of_vehicle = models.CharField(max_length=50, default='Double Cabin')
    brand = models.CharField(max_length=50, default='Toyota')
    carrying_capacity = models.CharField(max_length=50,
                                         default='4')

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
        Organisation, on_delete=models.CASCADE)
    fleet_manager = models.ForeignKey(
        FleetManager, on_delete=models.CASCADE)

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
        Organisation, on_delete=models.CASCADE)
    driver = models.ForeignKey(
        Driver, on_delete=models.CASCADE)

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
        Organisation, on_delete=models.CASCADE)

    vehicle = models.ForeignKey(
        Vehicle, on_delete=models.CASCADE)

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
    id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())
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

class Branch(BaseModel):
    id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())

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
    id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())
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
    id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())
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
    id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())
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
    id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())
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
        super(Directorate, self).save()

    def __str__(self):
        _str = '%s' % self.name
        return _str


class Blacklist(BaseModel):
    id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())
    organisation = models.ForeignKey(
        Organisation,  on_delete=models.CASCADE)

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
        Blacklist, on_delete=models.CASCADE)

    passenger = models.ForeignKey(
        Passenger, on_delete=models.CASCADE)
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
        Blacklist, on_delete=models.CASCADE)

    driver = models.ForeignKey(
        Driver, on_delete=models.CASCADE)
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
        Blacklist, on_delete=models.CASCADE)

    vehicle = models.ForeignKey(
        Vehicle, on_delete=models.CASCADE)
    reason = models.CharField(max_length=100)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(VehicleBlacklist, self).save()

    def __str__(self):
        _str = '%s' % self.vehicle.type_of_vehicle
        return _str

class Trip(BaseModel):
    id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())
    pick_up_location =models.CharField(max_length=100)
    date =models.DateField()
    time =models.TimeField()
    destination =models.CharField(max_length=100)
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
        super(Trip, self).save()
    def __str__(self):
        _str = '%s' % self.name
        return _str


class PassengerTrip(BaseModel):
    id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())
    pick_up_location =models.CharField(max_length=100)
    date =models.DateField()
    time =models.TimeField()
    destination =models.CharField(max_length=100)
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
        super(PassengerTrip, self).save()
    def __str__(self):
        _str = '%s' % self.name
        return _str

class DriverTrip(BaseModel):
    id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())
    pick_up_location =models.CharField(max_length=100)
    date =models.DateField()
    time =models.TimeField()
    destination =models.CharField(max_length=100)
    vehicle = models.ForeignKey(
        Vehicle, on_delete=models.CASCADE)
    reason = models.CharField(max_length=100)
    passenger = models.ForeignKey(
        Passenger,  on_delete=models.CASCADE)
    reason = models.CharField(max_length=100)
    driver = models.ForeignKey(
        Driver, on_delete=models.CASCADE)
    reason = models.CharField(max_length=100)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(DriverTrip, self).save()
    def __str__(self):
        _str = '%s' % self.name
        return _str


class FleetManagerTrip(BaseModel):
    id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())
    pick_up_location =models.CharField(max_length=100)
    date =models.DateField()
    time =models.TimeField()
    destination =models.CharField(max_length=100)
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
        _str = '%s' % self.name
        return _str

class ProjectVehicleDeploy(BaseModel):
    id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())
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
    id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())
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
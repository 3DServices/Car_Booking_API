from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from api.mixins.base_model_mixin import BaseModel
import uuid
from django.core.mail import send_mail
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db.models.signals import post_save


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given  email, and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)

        user.save()
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self,  email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=False,
        help_text=_(
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), blank=True, unique=True)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(
        _('staff status'),
        default=True,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    Id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())
    primary_contact = PhoneNumberField(default='+256777777777')
    secondary_contact = PhoneNumberField(default='+256777777777')
    # profile_photo =

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.Id = uuid.uuid4()
        super(User, self).save()

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


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
        _str = '%s' % self.user.email
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
        _str = '%s' % self.user.email
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
        _str = '%s' % self.user.email
        return _str


class Driver(models.Model):
    """

    """
    id = models.CharField(primary_key=True, max_length=50,
                          default=uuid.uuid4())
    permit_number = models.CharField(max_length=50,
                                     default='UAX')
    permit_class = models.CharField(max_length=50,
                                    default='UAX')

    permit_expiry_date = models.CharField(max_length=50,
                                          default='UAX')
    permit_issuance_date = models.CharField(max_length=50,
                                            default='UAX')
    user = models.OneToOneField(
        User, related_name="Driver", on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(Driver, self).save()

    def __str__(self):
        _str = '%s' % self.user.email
        return _str

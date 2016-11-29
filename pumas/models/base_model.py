import socket
import os
import pwd

from django_extensions.db.fields import UUIDField
from django.db.models import CharField
from django.utils.translation import ugettext as _

from django.db import models
from django_extensions.db.models import TimeStampedModel

BASE_MODEL_UPDATE_FIELDS = [
    'user_created', 'user_modified', 'hostname_created', 'hostname_modified']


class HostnameModificationField (CharField):

    description = _("Custom field for hostname modified")

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('blank', True)
        CharField.__init__(self, *args, **kwargs)

    def pre_save(self, model_instance, add):
        """Updates socket.gethostname() on each save."""
        value = socket.gethostname()
        setattr(model_instance, self.attname, value)
        return value


class UserField(CharField):

    description = _("Custom field for user created")

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('blank', True)
        CharField.__init__(self, *args, **kwargs)

    def get_os_username(self):
        return pwd.getpwuid(os.getuid()).pw_name

    def pre_save(self, model_instance, add):
        """Updates username created on ADD only."""
        value = super(UserField, self).pre_save(model_instance, add)
        if not value and not add:
            # fall back to OS user if not accessing through browser
            # better than nothing ...
            value = self.get_os_username()
            setattr(model_instance, self.attname, value)
            return value
        return value


class BaseModel(TimeStampedModel):

    """Base model class for all models. Adds created and modified'
    values for user, date and hostname (computer)."""

    uuid = UUIDField(editable=False, blank=True)

    get_latest_by = 'modified'

    user_created = UserField(
        max_length=50,
        verbose_name='user created',
        editable=False,
    )

    user_modified = UserField(
        max_length=50,
        verbose_name='user modified',
        editable=False,
    )

    hostname_created = models.CharField(
        max_length=50,
        editable=False,
        default=socket.gethostname(),
        help_text="System field. (modified on create only)",
    )

    hostname_modified = HostnameModificationField(
        max_length=50,
        editable=False,
        help_text="System field. (modified on every save)",
    )

    objects = models.Manager()

    def save(self, *args, **kwargs):
        try:
            # don't allow update_fields to bypass these audit fields
            update_fields = kwargs.get('update_fields', None) + BASE_MODEL_UPDATE_FIELDS
            kwargs.update({'update_fields': update_fields})
        except TypeError:
            pass
        super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True

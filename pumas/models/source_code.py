from django.db import models

from .user_profiles import Student


class SourceCode(models.Model):

    name = models.CharField(
        verbose_name='Name',
        max_length=15)

    author = models.OneToOneField(Student)

    year_of_pub = models.DateTimeField(
        verbose_name="Publication date time",
        null=True)

    class Meta:
        app_label = 'pumas'

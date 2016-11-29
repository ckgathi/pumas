from django.db import models

from .user_profiles import Student
from pumas.models.base_model import BaseModel


class SourceCode(BaseModel):

    name = models.CharField(
        verbose_name='Name',
        max_length=15)

    author = models.OneToOneField(Student)

    source_code_file = models.FileField(upload_to='source_code/')

    year_of_pub = models.DateTimeField(
        verbose_name="Publication date time",
        null=True)

    def __str__(self):
        return "{0}, {1}".format(self.name, self.author.user.username,)

    class Meta:
        app_label = 'pumas'

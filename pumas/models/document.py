from django.db import models
from django.contrib.auth.models import User

from pumas.choices import CATEGORY
from pumas.models.base_model import BaseModel
from pumas.models.source_code import SourceCode


class Document(BaseModel):

    title = models.CharField(
        verbose_name='Document title',
        max_length=250)

    author = models.ForeignKey(User)

    approved = models.BooleanField(default=False, editable=False)

    year_of_pub = models.DateTimeField(
        verbose_name="Publication date time")

    category = models.CharField(
        verbose_name='Category',
        choices=CATEGORY,
        max_length=250)

    source_code = models.ForeignKey(SourceCode)

    document = models.FileField(upload_to='documents/')

    abstract = models.TextField(verbose_name='Abstract')

    @property
    def year_of_publication(self):
        return self.year_of_pub.year

    class Meta:
        app_label = 'pumas'


class ProjectDocument(Document):

    def __str__(self):
        return "{0}, {1}".format(self.title, self.category)

    class Meta:
        app_label = 'pumas'


class Journal(Document):

    volume_number = models.IntegerField(
        verbose_name='Volume number')

    issue_number = models.IntegerField(
        verbose_name='Issue number')

    def __str__(self):
        return "{0}, {1}".format(self.title, self.category)

    class Meta:
        app_label = 'pumas'


class ConferencePreceeding(Document):

    reviewed = models.CharField(
        verbose_name='Reviewed',
        max_length=25)

    conference_name = models.CharField(
        verbose_name='Conference name',
        max_length=25)

    def __str__(self):
        return "{0}, {1}".format(self.title, self.category)

    class Meta:
        app_label = 'pumas'


class BookChapter(Document):

    pageNo = models.IntegerField(
        verbose_name='Page No')

    def __str__(self):
        return "{0}, {1}".format(self.title, self.category)

    class Meta:
        app_label = 'pumas'


class Dessertation(Document):

    def __str__(self):
        return "{0}, {1}".format(self.title, self.category)

    class Meta:
        app_label = 'pumas'


class Thesis(Document):

    def __str__(self):
        return "{0}, {1}".format(self.title, self.category)

    class Meta:
        app_label = 'pumas'

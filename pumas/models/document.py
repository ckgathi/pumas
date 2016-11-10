from django.db import models
from django.contrib.auth.models import User


class Document(models.Model):

    title = models.CharField(
        verbose_name='Document title',
        max_length=15)

    author = models.OneToOneField(User)

    year_of_pub = models.DateTimeField(
        verbose_name="Publication date time",
        null=True)

    category = models.CharField(
        verbose_name='Category',
        max_length=15)

    class Meta:
        app_label = 'pumas'


class ProjectDocument(Document):

    class Meta:
        app_label = 'pumas'


class Journal(Document):

    volume_number = models.IntegerField(
        verbose_name='Volume number')

    issue_number = models.IntegerField(
        verbose_name='Issue number')

    class Meta:
        app_label = 'pumas'


class ConferencePreceeding(Document):

    reviewed = models.CharField(
        verbose_name='Reviewed',
        max_length=25)

    conference_name = models.CharField(
        verbose_name='Conference name',
        max_length=25)

    class Meta:
        app_label = 'pumas'


class BookChapter(Document):

    pageNo = models.IntegerField(
        verbose_name='Page No')

    class Meta:
        app_label = 'pumas'


class TechnicalReport(Document):

    class Meta:
        app_label = 'pumas'


class Dessertation(Document):

    class Meta:
        app_label = 'pumas'


class Thesis(Document):

    class Meta:
        app_label = 'pumas'

from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):

    user = models.OneToOneField(User)

    student_id = models.IntegerField(
        verbose_name='Student Identifier',
        unique=True,
        help_text="Student identifier",
        editable=False,
        db_index=True)

    faculty = models.CharField(
        verbose_name="Faculty",
        max_length=150)

    programe = models.CharField(
        verbose_name="Programe of Study",
        max_length=150)

    class Meta:
        app_label = 'pumas'


class Lecture(models.Model):

    user = models.OneToOneField(User)

    stuff_id = models.IntegerField(
        verbose_name='Stuff Identifier',
        unique=True,
        help_text="Stuff identifier",
        db_index=True)

    is_supervisor = models.NullBooleanField(
        verbose_name='Are you a supervisor',
        default=False,)

    class Meta:
        app_label = 'pumas'


class Admin(models.Model):

    user = models.OneToOneField(User)

    stuff_id = models.IntegerField()

    class Meta:
        app_label = 'pumas'

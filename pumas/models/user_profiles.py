from django.db import models
from django.contrib.auth.models import User
from pumas.models.base_model import BaseModel


class Lecture(BaseModel):

    user = models.OneToOneField(User)

    staff_id = models.IntegerField(
        verbose_name='Stuff Identifier',
        unique=True,
        help_text="Stuff identifier",
        db_index=True)

    is_supervisor = models.NullBooleanField(
        verbose_name='Are you a supervisor',
        default=False,)

    def __str__(self):
        return "{0}, {1}".format(self.staff_id, self.user.username)

    class Meta:
        app_label = 'pumas'


class Student(BaseModel):

    user = models.OneToOneField(User)

    student_id = models.IntegerField(
        verbose_name='Student Identifier',
        unique=True,
        help_text="Student identifier",
        db_index=True)

    supervisor = models.ForeignKey(Lecture)

    faculty = models.CharField(
        verbose_name="Faculty",
        max_length=150)

    programe = models.CharField(
        verbose_name="Programe of Study",
        max_length=150)

    def __str__(self):
        return "{0}, {1}".format(self.student_id, self.user.username)

    class Meta:
        app_label = 'pumas'


class Admin(BaseModel):

    user = models.OneToOneField(User)

    staff_id = models.IntegerField()

    def __str__(self):
        return "{0}, {1}".format(self.staff_id, self.user.username)

    class Meta:
        app_label = 'pumas'

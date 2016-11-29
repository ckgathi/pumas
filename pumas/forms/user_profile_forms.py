from django import forms
from pumas.models.user_profiles import Student, Lecture, Admin


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'


class LectureForm(forms.ModelForm):

    class Meta:
        model = Lecture
        fields = '__all__'


class AdminForm(forms.ModelForm):

    class Meta:
        model = Admin
        fields = '__all__'

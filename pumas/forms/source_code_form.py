from django import forms
from pumas.models.source_code import SourceCode


class SourceCodeForm(forms.ModelForm):

    class Meta:
        model = SourceCode
        fields = '__all__'

from django import forms
from pumas.models.document import Document, Thesis, Dessertation, BookChapter, ConferencePreceeding, Journal,\
    ProjectDocument


class DocumentForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = '__all__'


class ProjectDocumentForm(forms.ModelForm):

    class Meta:
        model = ProjectDocument
        fields = '__all__'


class JournalForm(forms.ModelForm):

    class Meta:
        model = Journal
        fields = '__all__'


class ConferencePreceedingForm(forms.ModelForm):

    class Meta:
        model = ConferencePreceeding
        fields = '__all__'


class BookChapterForm(forms.ModelForm):

    class Meta:
        model = BookChapter
        fields = '__all__'


class DessertationForm(forms.ModelForm):

    class Meta:
        model = Dessertation
        fields = '__all__'


class ThesisForm(forms.ModelForm):

    class Meta:
        model = Thesis
        fields = '__all__'

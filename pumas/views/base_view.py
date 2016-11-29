from django.db.models import Q
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from pumas.forms import DocumentSearchForm
from pumas.models import Dessertation
from pumas.models.document import ProjectDocument, Thesis, Journal, BookChapter, ConferencePreceeding


class BaseView(TemplateView, FormView):

    form_class = DocumentSearchForm

    def form_valid(self, form, **kwargs):
        context = {}
        documents = []
        if form.is_valid():
            title = form.cleaned_data['title']
#             author = form.cleaned_data['author']
#             category = form.cleaned_data['category']
            try:
                dessertations = Dessertation.objects.filter(title__icontains=title)
                for dess in dessertations:
                    documents.append(dess)
            except Dessertation.DoesNotExist:
                form.add_error('document_title', 'document title not found. Please search again with a different title.')
            try:
                project_documents = ProjectDocument.objects.filter(title__icontains=title)
                for proj_doc in project_documents:
                    documents.append(proj_doc)
            except ProjectDocument.DoesNotExist:
                form.add_error('document_title', 'document title not found. Please search again with a different title.')
            try:
                thesis = Thesis.objects.filter(title__icontains=title)
                for thes in thesis:
                    documents.append(thes)
            except Thesis.DoesNotExist:
                form.add_error('document_title', 'document title not found. Please search again with a different title.')
            try:
                journals = Journal.objects.filter(title__icontains=title)
                for journal in journals:
                    documents.append(journal)
            except Journal.DoesNotExist:
                form.add_error('document_title', 'document title not found. Please search again with a different title.')
            try:
                bookchapters = BookChapter.objects.filter(title__icontains=title)
                for bookchapter in bookchapters:
                    documents.append(bookchapter)
            except BookChapter.DoesNotExist:
                form.add_error('document_title', 'document title not found. Please search again with a different title.')
            try:
                conferencepreceedings = ConferencePreceeding.objects.filter(title__icontains=title)
                for conferencepreceeding in conferencepreceedings:
                    documents.append(conferencepreceeding)
            except ConferencePreceeding.DoesNotExist:
                form.add_error('document_title', 'document title not found. Please search again with a different title.')
            context = self.get_context_data(**kwargs)
            context['form'] = form
            context.update({
                'documents': documents})
        return self.render_to_response(context)

from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.utils import timezone

from django.shortcuts import render

from pumas.views import BaseView


class ViewDocument(BaseView):

    def __init__(self):
        self.context = {}
        self.template_name = 'view_document.html'
        self.title = 'PUMAS'

    def get(self, request, *args, **kwargs):
        self.context.update({'form_class': self.form_class})
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        self.context.update({
            'title': self.title
        })
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        return super(ViewDocument, self).get_context_data(**kwargs)


class SearchResults(BaseView):

    def __init__(self):
        self.context = {}
        self.template_name = 'search_results.html'
        self.title = 'PUMAS'

    def get(self, request, *args, **kwargs):
        form = self.form_class(request.GET)
        if self.form_valid(form):
            pass
        self.context.update({
            'past_five_years': self.past_five_years,
            'content_types': self.content_types,
            'form_class': self.form_class})
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        self.context.update({
            'past_five_years': self.past_five_years,
            'content_types': self.content_types})
        return render(request, self.template_name, self.context)

    @property
    def past_five_years(self):
        current_year = timezone.now().year
        past_five_years = []
        n = 5
        while n > 0:
            past_five_years.append(current_year)
            current_year -= 1
            n -= 1
        return past_five_years

    @property
    def content_types(self):
        return [
            'book', 'journal', 'undergradute-project', 'gradute-project', 'articles', 'conference-preceeding',
            'book-chapter', 'technical-report', 'dessertation', 'thesis', 'project-document']

    def get_context_data(self, **kwargs):
        self.context = super(SearchResults, self).get_context_data(**kwargs)
        self.context.update({
            'past_five_years': self.past_five_years,
        })
        return self.context

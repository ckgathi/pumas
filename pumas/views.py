from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from django.shortcuts import render

from .forms import DocumentSearchForm
from .models import Dessertation


class BaseView(TemplateView, FormView):

    form_class = DocumentSearchForm

    def form_valid(self, form, **kwargs):
        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            category = form.cleaned_data['category']
            try:
                self.documents = Dessertation.objects.filter(title__icontains=title)
                print(self.documents, "here is the document obj")
            except Dessertation.DoesNotExist:
                form.add_error('document_title', 'document title not found. Please search again with a different title.')
            context = self.get_context_data(**kwargs)
            context['form'] = form
            context.update({
                'documents': self.documents})
        return self.render_to_response(context)


class HomeView(BaseView):

    def __init__(self):
        self.context = {}
        self.template_name = 'home.html'
        self.title = 'PUMAS'

    def get(self, request, *args, **kwargs):
        self.context.update({
            'form_class': self.form_class})
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        self.context.update({
        })
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context

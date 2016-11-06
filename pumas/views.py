from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from django.shortcuts import render

from .forms import DocumentSearchForm
from .models import Document


class HomeView(TemplateView, FormView):

    form_class = DocumentSearchForm

    def __init__(self):
        self.context = {}
        self.template_name = 'home.html'
        self.title = 'BHP FC'

    def get(self, request, *args, **kwargs):
        self.context.update({})
        return render(request, self.template_name, self.context)

    def form_valid(self, form):
        if form.is_valid():
            document_title = form.cleaned_data['document_title']
            try:
                self.documents = Document.objects.filter(document_title__icontains=document_title)
            except Document.DoesNotExist:
                form.add_error('document_title', 'document title not found. Please search again with a different title.')
            context = self.get_context_data(form=form)
            context.update({
                'documents': self.documents})
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.context.update({
        })
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        return super(HomeView, self).get_context_data(**kwargs)

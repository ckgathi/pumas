from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from pumas.forms import DocumentSearchForm
from pumas.models import Dessertation


class BaseView(TemplateView, FormView):

    form_class = DocumentSearchForm

    def form_valid(self, form, **kwargs):
        context = {}
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

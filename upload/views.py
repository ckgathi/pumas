from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from pumas.views.base_view import BaseView


class UploadView(BaseView):

    def __init__(self):
        self.context = {}
        self.template_name = 'upload.html'
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
        return super(UploadView, self).get_context_data(**kwargs)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UploadView, self).dispatch(*args, **kwargs)


class SupervisorUploadView(BaseView):

    def __init__(self):
        self.context = {}
        self.template_name = 'supervisor_uploiad_view.html'
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
        return super(SupervisorUploadView, self).get_context_data(**kwargs)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SupervisorUploadView, self).dispatch(*args, **kwargs)


class ApproveDocument(BaseView):

    def __init__(self):
        self.context = {}
        self.template_name = 'approve_document.html'
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
        return super(ApproveDocument, self).get_context_data(**kwargs)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ApproveDocument, self).dispatch(*args, **kwargs)

from django.shortcuts import render

from pumas.views.base_view import BaseView
from pumas.models.user_profiles import Lecture


class HomeView(BaseView):

    def __init__(self):
        self.context = {}
        self.template_name = 'home.html'
        self.title = 'PUMAS'

    def get(self, request, *args, **kwargs):
        supervisor = False
        if request.user.is_authenticated():
            try:
                lecture = Lecture.objects.get(user=request.user)
                supervisor = lecture.is_supervisor
            except Lecture.DoesNotExist:
                pass
        self.context.update({
            'form_class': self.form_class,
            'supervisor': supervisor})
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        self.context.update({
        })
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context

from braces.views import FormInvalidMessageMixin

from django.contrib.auth import authenticate, login
from django.contrib.auth.views import logout
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView

from pumas.forms.login_form import LoginForm


class LoginView(FormInvalidMessageMixin, FormView):
    template_name = "pumas/login.html"
    form_class = LoginForm
    success_url = '/home/'
    form_invalid_message = 'Invalid username or password.'

    def get(self, request, *args, **kwargs):
        logout(request)
#         if request.GET:
#             form = self.form_class(request.GET)
#             self.form_valid(form)
        return super(LoginView, self).get(request, *args, **kwargs)

    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        return super(LoginView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return self.request.GET.get('next', self.success_url)

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context.update({
            'form_class': self.form_class,
        })
        return context

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data.get('username'),
            password=form.cleaned_data.get('password'))
        if user:
            if user.is_active:
                login(self.request, user)
                return super(LoginView, self).form_valid(form)
        return self.form_invalid(form)

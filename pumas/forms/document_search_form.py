from django import forms

from crispy_forms.bootstrap import FieldWithButtons, StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field

from django.core.urlresolvers import reverse


class DocumentSearchForm(forms.Form):

    title = forms.CharField(
        label='Title',
        max_length=200)

    author = forms.CharField(
        label='Author',
        max_length=200)

    category = forms.CharField(
        label='Category',
        max_length=200)

    def __init__(self, *args, **kwargs):
        super(DocumentSearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper = FormHelper()
        self.helper.form_action = reverse('search_results_url')
        self.helper.form_id = 'form-subject-search'
        self.helper.form_method = 'post'
        self.helper.html5_required = True
        self.helper.layout = Layout(
            Field('title', css_class='input-xlarge'),
            Field('author', css_class='input-xlarge'),
            Field('category', css_class='input-xlarge'),
            FieldWithButtons(StrictButton('Search', css_class="btn btn-primary", type='submit')))

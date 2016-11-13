from django.conf.urls import url

from .views import ViewDocument, SearchResults

urlpatterns = [
    url(r'^view_document', ViewDocument.as_view(), name='view_document_url'),
    url(r'^search_results', SearchResults.as_view(), name='search_results_url'),
]

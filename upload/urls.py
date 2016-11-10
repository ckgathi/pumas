from django.conf.urls import url

from .views import UploadView, ViewDocument, SupervisorUploadView, ApproveDocument

urlpatterns = [
    url(r'^uploadfile', UploadView.as_view(), name='upload_url'),
    url(r'^view_document', ViewDocument.as_view(), name='view_document_url'),
    url(r'^supervisor_upload_view', SupervisorUploadView.as_view(), name='supervisor_upload_view_url'),
    url(r'^approve_document', ApproveDocument.as_view(), name='approve_document_url'),
]

from django.conf.urls import url

from .views import UploadView, SupervisorUploadView, ApproveDocument

urlpatterns = [
    url(r'^uploadfile', UploadView.as_view(), name='upload_url'),
    url(r'^supervisor_upload_view', SupervisorUploadView.as_view(), name='supervisor_upload_view_url'),
    url(r'^approve_document/(?P<id>[-\w]+)/$', ApproveDocument.as_view(), name='approve_document_url'),
]

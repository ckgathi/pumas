from django.conf.urls import url

from .views import UploadView

urlpatterns = [
    url(r'^uploadfile', UploadView.as_view(), name='upload_url'),
]

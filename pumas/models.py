from django.db import models


class Document(models.Model):

    document_title = models.CharField(
        verbose_name='Document title',
        max_length=15)

    class Meta:
        app_label = 'pumas'

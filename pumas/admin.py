
from django.contrib import admin

from .models import ProjectDocument, Journal, ConferencePreceeding, BookChapter, Dessertation, Thesis, Document
from .models import SourceCode, Student, Lecture, Admin

admin.site.register(Document)
admin.site.register(ProjectDocument)
admin.site.register(Journal)
admin.site.register(ConferencePreceeding)
admin.site.register(BookChapter)
admin.site.register(Dessertation)
admin.site.register(Thesis)

admin.site.register(Student)
admin.site.register(Lecture)
admin.site.register(SourceCode)
admin.site.register(Admin)

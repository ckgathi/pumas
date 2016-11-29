
from django.contrib import admin
from django.utils import timezone

from .models import ProjectDocument, Journal, ConferencePreceeding, BookChapter, Dessertation, Thesis, Document
from .models import SourceCode, Student, Lecture, Admin
from pumas.forms.ducument_form import DocumentForm, DessertationForm, ProjectDocumentForm, JournalForm,\
    ConferencePreceedingForm, BookChapterForm, ThesisForm
from pumas.forms.user_profile_forms import StudentForm, LectureForm, AdminForm
from pumas.forms.source_code_form import SourceCodeForm


class ModelAdminAuditFieldsMixin:

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user_created = request.user.username
            obj.created = timezone.now()
        else:
            obj.user_modified = request.user.username
            obj.modified = timezone.now()
        super(ModelAdminAuditFieldsMixin, self).save_model(request, obj, form, change)

    def get_list_filter(self, request):
        columns = ['created', 'modified', 'user_created', 'user_modified', 'hostname_created', 'hostname_modified']
        self.list_filter = list(self.list_filter or [])
        self.list_filter = self.list_filter + [item for item in columns if item not in self.list_filter]
        return tuple(self.list_filter)


class DocumentAdmin(ModelAdminAuditFieldsMixin, admin.ModelAdmin):
    form = DocumentForm
admin.site.register(Document, DocumentAdmin)


class DessertationAdmin(ModelAdminAuditFieldsMixin, admin.ModelAdmin):
    form = DessertationForm

    def image_img(self):
        if self.document:
            return u'<img src="%s" />' % self.document.url
        else:
            return '(No image found)'
admin.site.register(Dessertation, DessertationAdmin)


class ProjectDocumentAdmin(ModelAdminAuditFieldsMixin, admin.ModelAdmin):
    form = ProjectDocumentForm
admin.site.register(ProjectDocument, ProjectDocumentAdmin)


class JournalAdmin(ModelAdminAuditFieldsMixin, admin.ModelAdmin):
    form = JournalForm
admin.site.register(Journal, JournalAdmin)


class ConferencePreceedingAdmin(ModelAdminAuditFieldsMixin, admin.ModelAdmin):
    form = ConferencePreceedingForm
admin.site.register(ConferencePreceeding, ConferencePreceedingAdmin)


class BookChapterAdmin(ModelAdminAuditFieldsMixin, admin.ModelAdmin):
    form = BookChapterForm
admin.site.register(BookChapter, BookChapterAdmin)


class ThesisAdmin(ModelAdminAuditFieldsMixin, admin.ModelAdmin):
    form = ThesisForm
admin.site.register(Thesis, ThesisAdmin)


class StudentAdmin(ModelAdminAuditFieldsMixin, admin.ModelAdmin):
    form = StudentForm
admin.site.register(Student, StudentAdmin)


class LectureAdmin(ModelAdminAuditFieldsMixin, admin.ModelAdmin):
    form = LectureForm
admin.site.register(Lecture, LectureAdmin)


class SourceCodeAdmin(ModelAdminAuditFieldsMixin, admin.ModelAdmin):
    form = SourceCodeForm
admin.site.register(SourceCode, SourceCodeAdmin)


class AdminAdmin(ModelAdminAuditFieldsMixin, admin.ModelAdmin):
    form = AdminForm
admin.site.register(Admin, AdminAdmin)

from django.contrib import admin
from iiitm.models import Complaint, Library, BooksIssued, FacultyStatus
from django.contrib.auth.models import User

# Register your models here.

class ComplaintAdmin(admin.ModelAdmin):
	list_display = ('type_of_complaint', 'complaint_subject', 'solved', 'preference')

class BooksIssuedAdmin(admin.ModelAdmin):
	list_display = ('name', 'username', 'duedate')

admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Library)
admin.site.register(BooksIssued, BooksIssuedAdmin)

admin.site.register(FacultyStatus)
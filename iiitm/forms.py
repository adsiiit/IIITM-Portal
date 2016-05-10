from django import forms
from django.contrib.auth.models import User
from iiitm.models import Complaint, Library, FacultyStatus


#Complaint Form
class ComplaintsForm(forms.ModelForm):

	class Meta:
		model = Complaint
		exclude = ('user','solved','comment','preference')


#Complaint Status Form
class StatusForm(forms.Form):
    idnumber = forms.IntegerField()

    def clean_idnumber(self):
		idnumber = self.cleaned_data['idnumber']
		try:
			Complaint.objects.get(pk=idnumber)
			return idnumber
		except Complaint.DoesNotExist:
			raise forms.ValidationError("This Complaint ID doesn't exist. Enter Valid one !!")


#Book Status Form

class BookForm(forms.Form):
	bookid = forms.CharField()

	def clean_bookid(self):
		bookid = self.cleaned_data['bookid']
		try:
			Library.objects.get(bookid=bookid)
			return bookid
		except Library.DoesNotExist:
			raise forms.ValidationError("This Book doesn't exist. Select a valid one")


class FacultyForm(forms.Form):
	facid = forms.IntegerField()

	def clean_facid(self):
		facid = self.cleaned_data['facid']
		try:
			FacultyStatus.objects.get(id=facid)
			return facid
		except FacultyStatus.DoesNotExist:
			raise forms.ValidationError("Select a valid one")



class SetForm(forms.ModelForm):

	class Meta:
		model = FacultyStatus
		exclude = ('username','name')

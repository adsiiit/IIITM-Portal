from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from iiitm.forms  import ComplaintsForm, StatusForm, BookForm, FacultyForm
from iiitm.models import Complaint, Library, BooksIssued, FacultyStatus

# Create your views here.
def index(request):
	return render(request, 'index.html', {})

def about(request):
	return render(request, 'iiitm/aboutus.html', {})

def activities(request):
	return render(request, 'iiitm/activities.html', {})



@login_required
def add_complaint(request):
	user = request.user
	if request.method == 'POST':
		form = ComplaintsForm(request.POST) 
		if form.is_valid():
			forid = form.save(commit=True)
			valueid = forid.id
			
			# After submission of complaint user will be shown homepage
			return render(request, 'iiitm/after_complaint.html', {'valueid':valueid})
		else:
			print form.errors
	else:
		# If the request was not a POST, display the form to enter details.
		form = ComplaintsForm()

	return render(request, 'iiitm/add_complaint.html', {'form': form,'user':user})


def complaint_status(request):
	if request.method == 'POST':
			form = StatusForm(request.POST) 
			if form.is_valid():
				cd = form.cleaned_data['idnumber']
				#idnumber  = cd.get('idnumber')
				status = Complaint.objects.get(pk=cd)
				form = StatusForm()
				# After submission of complaint user will be shown homepage
				return render(request, 'iiitm/complaint_status.html', {'form':form, 'status':status})
			
	else:
			# If the request was not a POST, display the form to enter details.
		form = StatusForm()

	return render(request, 'iiitm/complaint_status.html', {'form':form})




def library_status(request):
	obj = Library.objects.all().order_by('name')
	if request.method == 'POST':
		form = BookForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data['bookid']
			
			status = Library.objects.get(bookid=cd)
			form = BookForm()
			return render(request, 'iiitm/library_status.html',{'form':form, 'status':status, 'obj':obj})

	else:
			# If the request was not a POST, display the form to enter details.
		form = BookForm()

	return render(request, 'iiitm/library_status.html', {'form':form, 'obj':obj})



@login_required
def issue_status(request):
	user = request.user
	try:
		obj = BooksIssued.objects.all().filter(username=user.username)
	except:
		obj = ''

	return render(request, 'iiitm/issue_status.html',{'obj':obj})



@login_required
def accounts(request):
	user = request.user

	return render(request, 'iiitm/accounts.html',{})


@login_required
def administration(request):
	user = request.user

	return render(request, 'iiitm/administration.html',{})



def faculty_status(request):
	obj = FacultyStatus.objects.all().order_by('name')
	if request.method == 'POST':
		form = FacultyForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data['facid']
			stat = FacultyStatus.objects.get(pk=cd)
			form = FacultyForm()
			return render(request, 'iiitm/faculty_status.html',{'form':form, 'stat':stat, 'obj':obj})

	else:
			# If the request was not a POST, display the form to enter details.
		form = FacultyForm()

	return render(request, 'iiitm/faculty_status.html', {'form':form, 'obj':obj})



@login_required
def academics(request):
	user = request.user
	info = request.user.userprofile

	return render(request, 'iiitm/academics.html',{'info':info, 'user':user})
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from registration.models import UserProfile
from registration.forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from iiitm.models import BooksIssued, FacultyStatus
import datetime
from django.utils import timezone
from iiitm.forms import SetForm


# def index(request):
# 	if not request.user.is_authenticated():
# 		return render(request, 'base.html', {})
# 	else:
# 		info = request.user.userprofiles
# 		context = {'info':info}
# 		return render_to_response('base.html', context, context_instance=RequestContext(request))


def register(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/profile/')
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(username=form.cleaned_data['username'], email = form.cleaned_data['email'], password=form.cleaned_data['password'])
			user.save()

			registration = UserProfile(user=user, name = form.cleaned_data['name'],	address = form.cleaned_data['address'],
				contact = form.cleaned_data['contact'], stream = form.cleaned_data['stream'], age = form.cleaned_data['age'], 
				gender = form.cleaned_data['gender'], register_as = form.cleaned_data['register_as']
				)

			if form.cleaned_data['register_as']=='FY':
				facstat = FacultyStatus(username = form.cleaned_data['username'], name = form.cleaned_data['name'])
				facstat.save()

			if 'picture' in request.FILES:
				registration.picture = request.FILES['picture']

			registration.save()
			return HttpResponseRedirect('/profile')

		else:
			return render_to_response('registration/register.html',{'form':form, 're':"active"}, context_instance=RequestContext(request))


	else:
	 	form = RegistrationForm()
	   	context = {'form': form, 're':"active"}
	  	return render_to_response('registration/register.html', context, context_instance=RequestContext(request))

@login_required
def profile(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('registration/login/')

	user = request.user
	try:
		obj = BooksIssued.objects.all().filter(username=user.username)
	except:
		obj = None

	lib = False

	if obj is not None:
		for ob in obj:
			if ob.duedate < timezone.now() + datetime.timedelta(days=1):
				lib = True


	info = request.user.userprofile
	#context = {'info':info, 'lib':lib}


	#status by faculty
	

	if info.register_as == 'FY':
		objec = FacultyStatus.objects.get(username = user.username)
		if request.method == 'POST':
			form = SetForm(request.POST)
			if form.is_valid():
				objec.subject = form.cleaned_data['subject']
				objec.status = form.cleaned_data['status']
				objec.message = form.cleaned_data['message']
				objec.save()
				return render_to_response('registration/profile.html',{'form':form, 'info':info, 'lib':lib, 'objec':objec}, context_instance=RequestContext(request))


		else:
		 	form = SetForm()
		   	context = {'form': form, 'info':info, 'lib':lib, 'objec':objec}
		  	return render_to_response('registration/profile.html', context, context_instance=RequestContext(request))


	
	return render_to_response('registration/profile.html', {'info':info, 'lib':lib}, context_instance=RequestContext(request))



def loginrequest(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/profile/')
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			signin = authenticate(username=username, password=password)
			if signin is not None:
				login(request, signin)
				return HttpResponseRedirect('/profile/')
			else:
				return render_to_response('registration/login.html', {'form':form, 'ln':"active"}, context_instance=RequestContext(request))
		else:
			return render_to_response('registration/login.html', {'form':form, 'ln':"active"}, context_instance=RequestContext(request))

		
	else:
		form = LoginForm()
		context = {'form': form, 'ln':"active"}
		return render_to_response('registration/login.html', context, context_instance=RequestContext(request))


def logoutrequest(request):
	logout(request)
	return render(request, 'registration/logout.html', {})


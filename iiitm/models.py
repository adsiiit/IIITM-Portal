from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta


# Create your models here.
class Complaint(models.Model):

	username = models.CharField(max_length=128)
	ACADEMICS = 'AC'
	ACCOUNTS = 'AT'
	ADMINISTRATION = 'AD'
	HOSTEL = 'HO'
	HOSPITAL = 'HP'
	LIBRARY = 'LI'
	MISSING = 'MI'
	OTHERS = 'OT'

	TYPEOFCOMP_CHOICES = (
		(ACADEMICS, 'Academics'),
		(ACCOUNTS, 'Accounts'),
		(ADMINISTRATION, 'Administration'),
		(HOSTEL, 'Hostel'),
		(HOSPITAL, 'Hospital'),
		(LIBRARY, 'Library'),
		(MISSING, 'Missing'),
		(OTHERS, 'Others'),
		)
	type_of_complaint = models.CharField(max_length=2,
									choices=TYPEOFCOMP_CHOICES,
									default=OTHERS)


	complaint_subject = models.CharField(max_length=200)
	complaint_desc = models.TextField()

	SOLVED='SOLVED'
	UNSOLVED='NOT SOLVED'
	CON = 'UNDER CONSIDERATION'
	SOLVED_CHOICES = (
		(SOLVED, 'Solved'),
		(UNSOLVED, 'Unsolved'),
		(CON, 'Under Consideration')
		)
	solved = models.CharField(max_length=50,
							choices=SOLVED_CHOICES,
							default=UNSOLVED)
	comment = models.TextField()

	PREFERENCE_CHOICE = (
		(1, 1),
		(2, 2),
		(3, 3),
		(4, 4),
		(5, 5),
		) 
	preference = models.IntegerField(choices=PREFERENCE_CHOICE,
									default=0)

	def __unicode__(self):
		return self.type_of_complaint




class Library(models.Model):

	name = models.CharField(max_length=128)
	author = models.CharField(max_length=128)
	bookid = models.CharField(max_length=128)
	quantity = models.IntegerField(default=0)
	available = models.IntegerField(default=0)

	def __unicode__(self):
		return self.bookid



class BooksIssued(models.Model):

	name = models.CharField(max_length=128)
	unitid = models.CharField(max_length=128)
	username = models.CharField(max_length=128)
	issuedate = models.DateTimeField(default=datetime.now())
	duedate = models.DateTimeField(default=datetime.now()+timedelta(days=10))

	def __unicode__(self):
		return self.name



class FacultyStatus(models.Model):

	username = models.CharField(max_length=128)
	name = models.CharField(max_length=128)

	
	AVAILABLE='AVAILABLE'
	UNAVAILABLE='NOT AVAILABLE'
	NOTCONFIRM = 'NOT CONFIRM'
	STATUS_CHOICES = (
		(AVAILABLE, 'AVAILABLE'),
		(UNAVAILABLE, 'NOT AVAILABLE'),
		(NOTCONFIRM, 'NOT CONFIRM')
		)

	subject = models.CharField(max_length=50, default="None")
	status = models.CharField(max_length=50,
							choices=STATUS_CHOICES,
							default=NOTCONFIRM)

	message = models.TextField(default="NOTHING")

	def __unicode__(self):
		return self.name
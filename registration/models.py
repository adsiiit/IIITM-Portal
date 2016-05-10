from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	#reenter_password = models.CharField(max_length=200)
	

	name = models.CharField(max_length=128)
	MALE = 'M'
	FEMALE = 'F'
	SELECT = 'N'
	GENDER_CHOICES = (
		(SELECT, 'SELECT'),
		(MALE, 'Male'),
		(FEMALE, 'Female'),
		)
	gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default=SELECT)
	age = models.IntegerField(default=0)
	address = models.CharField(max_length=1024)
	contact = models.BigIntegerField(unique=True)

	IPG = 'IPG'
	MTECH = 'MTECH'
	MBA = 'MBA'
	PHD = 'PHD'
	NONE = 'NONE'
	OTHER = 'OTHER'


	STREAM_CHOICES = (
		(IPG, 'IPG'),
		(MTECH, 'MTECH'),
		(MBA, 'MBA'),
		(PHD, 'PHD'),
		(OTHER, 'OTHER'),
		(NONE, 'NONE')
		)
	stream = models.CharField(max_length=6,
							choices=STREAM_CHOICES,
							default=NONE)


	FACULTY = 'FY'
	STUDENT = 'ST'
	STAFF = 'SF'
	OTHER = 'OR'

	REGISTER_AS_CHOICES = (
		(FACULTY, 'FACULTY'),
		(STUDENT, 'STUDENT'),
		(STAFF, 'STAFF'),
		(OTHER, 'OTHER'),
		)

	register_as = models.CharField(max_length=2,
							choices=REGISTER_AS_CHOICES,
							default=OTHER)

	picture = models.ImageField(upload_to = "profile_images/", blank=True)

	def __unicode__(self):
		return self.user.username
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models import signals
from django.db.models.signals import post_save
from django.dispatch import receiver
from vote.managers import VotableManager

class UserProfile(models.Model):
	    #required by the auth model
	user = models.ForeignKey(User, unique=True)
	status = models.IntegerField(default=0)
#url = models.URLField()
#home_address = models.TextField()

class Event(models.Model):
	event=models.TextField()
	organiser=models.TextField()
	attachment = models.FileField(upload_to='events/%Y/%m/%d',blank=True)

class Publications(models.Model):
	votes = VotableManager(blank=True)
	document_id = models.TextField(blank=True)
	project_title = models.TextField(blank=True)
	department_name = models.TextField(blank=True)
	name_1 = models.TextField(blank=True)
	designation_1 = models.TextField(blank=True)
	email_1 = models.TextField(blank=True)
	address_1 = models.TextField(blank=True)
	phone_1 = models.TextField(blank=True)
	fax_1 = models.TextField(blank=True)
	mobile_1 = models.TextField(blank=True)
	name_2 = models.TextField(blank=True)
	designation_2 = models.TextField(blank=True)
	email_2 = models.TextField(blank=True)
	address_2 = models.TextField(blank=True)
	phone_2 = models.TextField(blank=True)
	fax_2 = models.TextField(blank=True)
	mobile_2 = models.TextField(blank=True)
	category = models.TextField(blank=True)
	nature = models.TextField(blank=True)
	description = models.TextField(blank=True)
	date = models.TextField(blank=True)
	url = models.TextField(blank=True)
	business_model = models.TextField(blank=True)
	no_process = models.TextField(blank=True)
	beneficiary_1 = models.TextField(blank=True)
	beneficiary_2 = models.TextField(blank=True)
	beneficiary_3 = models.TextField(blank=True)
	transaction = models.TextField(blank=True)
	benefit_1 = models.TextField(blank=True)
	benefit_2 = models.TextField(blank=True)
	benefit_3 = models.TextField(blank=True)
	process_1 = models.TextField(blank=True)
	process_2 = models.TextField(blank=True)
	process_3 = models.TextField(blank=True)
	database = models.TextField(blank=True)
	operating = models.TextField(blank=True)
	web_server = models.TextField(blank=True)
	prime_agency = models.TextField(blank=True)
	network_arrangement = models.TextField(blank=True)
	datacenter = models.TextField(blank=True)
	csc = models.TextField(blank=True)
	formal_document = models.TextField(blank=True)
	implementation = models.TextField(blank=True)
	no_training = models.TextField(blank=True)
	sector = models.TextField(blank=True)
	sub_sector = models.TextField(blank=True)
	state = models.TextField(blank=True)	
	attachment = models.FileField(upload_to='%Y/%m/%d',blank=True)

class Recepient(models.Model):
	user = models.ManyToManyField(User)
   	name=models.CharField(max_length=200)
	address=models.CharField(max_length=200)
	contact=models.CharField(max_length=10)
	bggroup=models.CharField(max_length=2)
	email=models.CharField(max_length=100)
	bgunits=models.IntegerField(blank=True)
	age=models.IntegerField(blank=True)
	lat1=models.FloatField(blank=True,null=True)
	long1=models.FloatField(blank=True,null=True)

class Donor(models.Model):
	user = models.ManyToManyField(User)
	name=models.CharField(max_length=200)
	address=models.CharField(max_length=200)
	contact=models.CharField(max_length=10)
	bggroup=models.CharField(max_length=2)
	email=models.CharField(max_length=100)
	bgunits=models.IntegerField(blank=True)
	age=models.IntegerField(blank=True)
	lat1=models.FloatField(blank=True,null=True)
	long1=models.FloatField(blank=True,null=True)

class Hospital(models.Model):
	contact=models.CharField(max_length=10)
	address=models.CharField(max_length=200)
	name=models.CharField(max_length=200)
	abgroup=models.CharField(max_length=200)

class Camp(models.Model):
	name=models.CharField(max_length=200)
	email=models.CharField(max_length=100)
	contact=models.CharField(max_length=10)
	address=models.CharField(max_length=200)	
	uid=models.IntegerField()
	cdate = models.CharField(max_length=200)
	sdate=models.CharField(max_length=200)
	edate=models.CharField(max_length=200)
	lat1=models.FloatField(blank=True,null=True)
	long1=models.FloatField(blank=True,null=True)

class Link(models.Model):
	uid=models.IntegerField()
	cid=models.IntegerField()
	guser=models.CharField(max_length=200)
	flag=models.IntegerField(blank=True)

class Post(models.Model):
	uid = models.IntegerField()
	#user=models.ForeignKey(User)
	comment=models.CharField(max_length=200)
	campid=models.CharField(max_length=200)

class Story(models.Model):
	suser = models.ManyToManyField(User)
	story=models.CharField(max_length=200)
	tag=models.CharField(max_length=200)
	#pic=models.ImageField(upload_to="static",blank=True)

class Notification(models.Model):
	did = models.ManyToManyField(User)
	#did=models.ForeignKey(User)
	rid=models.CharField(max_length=200)
	flag=models.IntegerField(blank=True)

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

class Choice(models.Model):
	question = models.ManyToManyField(Question)
    	#question = models.ForeignKey(Question)
    	choice_text = models.CharField(max_length=200)
    	votes = models.IntegerField(default=0)

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	# Creates user profile
	if created:
		profile, new = UserProfile.objects.get_or_create(user=instance)

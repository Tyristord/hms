from django.db import models

# Create your models here.
class Doctor_details(models.Model):
	"""docstring for Doctor_details"""
	name = models.CharField(max_length = 200, null = True)
	quali = models.CharField(max_length = 200, null = True)
	spec = models.CharField(max_length = 200, null = True)
	contact_no = models.IntegerField(default = 0)
	mail_id = models.CharField(max_length = 200, null = True)
	password = models.CharField(max_length = 250, null = True)
	active  = models.IntegerField(default = 0)
	available = models.CharField(max_length = 250, null = True)
	rating = models.IntegerField(default = 0)
	trusted = models.CharField(max_length = 250, null = True)
	online = models.CharField(max_length = 250, null = True)
	seniority = models.CharField(max_length = 250, null = True)
	hospital = models.CharField(max_length = 250, null = True)
	experience = models.CharField(max_length = 250, null = True)
	fee = models.IntegerField(default = 0)
	address = models.CharField(max_length = 250, null = True)


'''

24 hrs available

[1:10] 
independent or hospital

[1:10] 
qualification

[1:10] 
experience

[1:11] 
rating

[1:11] 
availiable dates and times

[1:11] 
trusted/honured

[1:11] 
online

[1:11] 
seniority level '''
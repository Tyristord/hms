from django.db import models

# Create your models here.
class Patient_details(models.Model):
	"""docstring for Patient_details"""
	patient_id = models.CharField(max_length = 200, null = True)
	patient_name = models.CharField(max_length = 200, null = True)
	insurance_no = models.CharField(max_length = 200, null = True)
	insurance_provider = models.CharField(max_length = 200, null = True)
	insurance_policy = models.CharField(max_length = 200, null = True)
	insurance_enquiry = models.CharField(max_length = 200, null = True)
	patient_address = models.CharField(max_length = 200, null = True)
	mail_id = models.CharField(max_length = 200, null = True)
	contact_no = models.IntegerField(default = 0)
	age = models.IntegerField(default = 0)
	password = models.CharField(max_length = 250, null = True)
	#health_id = models.ForeignKey(health_id)
	
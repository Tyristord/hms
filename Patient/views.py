from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import Context, loader
from django.http import HttpResponse
from models import Patient_details
# Create your views here.

def index(request):
	return render_to_response('home/index.html')
def account_detail(request):
	info = Patient_details.objects.all()
	context = Context({'info': info})
	return render(request,'patient/dashboard.html',context)
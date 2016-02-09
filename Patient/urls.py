from django.conf.urls import include, url
from . import views


urlpatterns = [
url(r'^$',views.index,name='Patient'),
url(r'^patient/dashboard',views.account_detail,name= 'Patient'),
]
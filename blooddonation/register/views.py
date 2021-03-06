# Create your views here.
from django.shortcuts import render
from register.models import *
from register.forms import *
from django.core.mail import send_mail

def index(request):
	if request.user.is_authenticated():
		if request.method == 'POST':
			yourname = request.POST['yourname']
			#print uname
			
			bloodgroup = request.POST['bloodgroup']
			phone = request.POST['phone']
			email = request.POST['email']
			
			#print list
			#print type(entry.c)
			#for element in list:
			#	print list[element]
			form1 = Register.objects.create(yourname = yourname,bloodgroup = bloodgroup, phone = phone , email = email)
			form = c_form(
				initial={'yourname':"Your Name here",'bloodgroup':"Your bloodgroup here",'phone':"Phone number  here",'email':"E-mail here"}
				)
			form1.save()
			return render(request, 'blooddonation/index1.html')
			
		else:
			form = c_form(
				initial={'yourname':"Your Name here",'bloodgroup':"Your bloodgroup here",'phone':"Phone number  here",'email':"E-mail here"}
				)
			return render(request,'register/index.html', {'form':form})
		
	
	else:
		return render(request, 'blooddonation/index.html')

def raiserequest(request):
	if request.user.is_authenticated():
		if request.method == 'POST':
			patientname = request.POST['patientname']
			#print uname
			
			bloodgroupreqd = request.POST['bloodgroupreqd']
			phone1 = request.POST['phone1']
			email1 = request.POST['email1']
			volunteername = request.POST['volunteername']
			volunteerbloodgroup = request.POST['volunteerbloodgroup']
			#print list
			#print type(entry.c)
			#for element in list:
			#	print list[element]
			form1 = Raiserequests.objects.create(patientname = patientname,bloodgroupreqd = bloodgroupreqd, phone1 = phone1 , email1 = email1, volunteername = volunteername, volunteerbloodgroup = volunteerbloodgroup)
			form = req_form(
				initial={'patientname':"Your Name here",'bloodgroupreqd':"Your bloodgroup here",'phone1':"Phone number  here",'email1':"E-mail here", 'volunteername':"Volunteer name here", 'volunteerbloodgroup':"Blood group of volunteer"}
				)
			form1.save()
			instance = blood.objects.get(group=bloodgroupreqd)
			instance1 = blood.objects.get(group=volunteerbloodgroup)
			if instance.count >=1:
				
				instance.count -= 1
				instance1.count += 1
				instance.save()
				instance1.save()
				return render(request, 'register/requestok.html')
			else:
				for p in Register.objects.raw('SELECT email FROM register_register'):
#					print p.email, p.yourname
#					print type(p)
					for i in range(1,100):
						send_mail('BloodDonate:Urgent Blood requirement', 'Urgently required '+bloodgroupreqd+' blood. Please spread the word. Contact us asap.', 'blooddonatebyld@gmail.com', [p.email]) 
				return render(request, 'register/requestnull.html')
			
		else:
			form = req_form(
				initial={'patientname':"Your Name here",'bloodgroupreqd':"Your bloodgroup here",'phone1':"Phone number  here",'email1':"E-mail here", 'volunteername':"Volunteer name here", 'volunteerbloodgroup':"Blood group of volunteer"}
				)
			return render(request,'register/raiserequest.html', {'form':form})
		
	
	else:
		return render(request, 'blooddonation/index.html')

def volunteer(request):
	if request.user.is_authenticated():
		if request.method == 'POST':
			
			volunteername1 = request.POST['volunteername1']
			bloodgroup1 = request.POST['bloodgroup1']
			phone2 = request.POST['phone2']
			#print list
			#print type(entry.c)
			#for element in list:
			#	print list[element]
			form1 = Volunteers.objects.create( volunteername1 = volunteername1, bloodgroup1 = bloodgroup1, phone2 = phone2 )
			form = vol_form(
				initial={'volunteername1':"Volunteer name here" ,'bloodgroup1':"Your bloodgroup here",'phone2':"Phone number here" }
				)
			
			instance = blood.objects.get(group=bloodgroup1)
			instance.count +=1
			instance.save()
			
			form1.save()
			return render(request, 'register/volunteercertificate.html')
			
		else:
			form = vol_form(
				initial={'volunteername1':"Volunteer name here" ,'bloodgroup1':"Your bloodgroup here",'phone2':"Phone number here"}
				)
			return render(request,'register/volunteer.html', {'form':form})
		
	
	else:
		return render(request, 'blooddonation/index.html')

def drive(request):
	return render(request, 'register/drive.html')

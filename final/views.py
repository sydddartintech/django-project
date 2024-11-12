from django.http import HttpResponse
from django.shortcuts import render,redirect
from final import models
from django.contrib import messages
def home(request):
	return render(request,"newhome/index.html")


def login(request):
    return render(request, "loginpage/login.html")

def check_login(request):
    if request.method == 'POST':
        uname = request.POST['email']
        password = request.POST['password']
        log_info = models.Login.objects.filter(username=uname, password=password)

        if log_info.exists():
            for log in log_info:
                if log.username == uname and log.password == password:
                    if log.user_type == 'admin' and log.status == 'active':
                        request.session['semail'] = log.username
                        return redirect("../administrator/admin")

                    elif log.user_type == 'Service_provider' and log.status == 'active':
                        request.session['semail'] = log.username
                        return redirect("../serviceprovider/servicehome")

                    elif log.user_type=='Client':
                        request.session['semail'] = log.username
                        return redirect("../client/clienthome")
        # If the login does not exist or user is inactive, redirect to the login page
        return redirect('login')
    else:
        return redirect('login')	

# def check_login(request):
# 	uname=request.POST['email']
# 	password=request.POST['password']
# 	log_info=models.Login.objects.filter(username=uname,password=password)
# 	for log in log_info:
# 		if log.username == uname and log.password == password:
# 			if log.user_type=='admin' and log.status=='active':
# 				request.session['semail']=log.username
# 				return redirect("../administrator/admin")
			
# 			elif log.user_type=='Service_provider' and log.status=='active':
# 				request.session['semail']=log.username
# 				return redirect("../serviceprovider/servicehome")
# 			else:
# 				return redirect("../loginpage/login.html")



def dash(request):
	return render(request,"admin/dashboard.html")
def reg(request):
	return render(request,"registration/reg.html")

def savereg(request):
	sdata=models.Registration.objects.all()
	context={
	'slist':sdata
	}
	return render(request,"registration/reg.html",context)

def saveregister(request):
	name=request.POST['name']
	address=request.POST['address']
	state=request.POST['state']
	district=request.POST['district']
	city=request.POST['city']
	phone=request.POST['phone']
	email=request.POST['email']
	password=request.POST['password']
	sdata=models.Registration(reg_name=name,address=address,state=state,district=district,city=city,phone_number=phone,email_id=email)
	sdata.save()

	logindata=models.Login(username=email,password=password,user_type='Service_provider',status='inactive')
	logindata.save()
	return redirect("registration")

	#client side>>>

def client_reg(request):
	return render(request,"client/client_reg.html")

def save_cli(request):
	sdata=models.Registration.objects.all()
	context={
	'slist':sdata
	}
	return render(request,"client/client_reg.html",context)


def c_register(request):
	name=request.POST['name']
	address=request.POST['address']
	state=request.POST['state']
	district=request.POST['district']
	city=request.POST['city']
	phone=request.POST['phone']
	email=request.POST['email']
	password=request.POST['password']
	sdata=models.Registration(reg_name=name,address=address,state=state,district=district,city=city,phone_number=phone,email_id=email)
	sdata.save()

	logindata=models.Login(username=email,password=password,user_type='Client',status='inactive')
	logindata.save()
	return redirect("registration")






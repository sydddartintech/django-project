from django.shortcuts import render,redirect
from final import models
from django.http import HttpResponse

# Create your views here.
def clienthome(request):

	return render(request,"client/home.html")

def changepsw(request):
	return render(request,"client/changepsw.html")

def change_pass_client(request):
	npass=request.POST['newpsw']
	cpass=request.POST['confpsw']
	uname=request.session['semail']
	
	if npass==cpass:
		
		log=models.Login.objects.get(username=uname)
		log.password=npass
		log.save()
		return redirect("login")
	else:
		return redirect("change_pass")

def client_profile(request):
	pname=request.session['semail']
	register=models.Registration.objects.all()
	context={
	'register':register
	}
	return render(request,"client/profile.html",context)

def editclient(request,reg_id):
	register=models.Registration.objects.get(pk=reg_id)
	context={
	'register': register
	}
	return render(request, "client/editclient.html", context)

def updateclient(request):
	name=request.POST['name']
	email=request.POST['email']
	address=request.POST['address']
	reg_id=request.POST['reg_id']
	# return HttpResponse(name)
	newdata=models.Registration.objects.get(pk=reg_id)
	newdata.reg_name=name
	newdata.email_id=email
	newdata.address=address
	newdata.save()
	return redirect("client_profile")

def view_service_provider(request):
	view_account=models.AccountDetails.objects.all()
	context={
	'view_account':view_account
	}
	return render(request,"client/view_service_provider.html",context)

def log_out_c(request):
	return render(request,"newhome/index.html")



def profile(request):
	pname=request.session['semail']
	register=models.Registration.objects.get(email_id=pname)
	# return HttpResponse(pname)
	context={
	'register':register
	}
	return render(request,"client/profile.html",context)




# def seeportfolio(request):
# 	portfolio=models.Portfolio.objects.all()
# 	context={
# 	'portfolio':portfolio
# 	}
# 	return render(request,"client/seeportfolio.html",context)

# def search_sp(request):
# 	cat1=request.POST['category']
# 	new=models.Category.objects.all()
# 	context={
# 	'cat1':new
# 	}
# 	return render(request,"client/client_want_sp.html",context)



def go_to_sp(request):
	client=models.Projects.objects.all()
	context={
	'client':client
	}
	# return HttpResponse(client)
	return render(request,"client/cat.html",context)

# def client_want_sp(request):
	
# 	return render(request,"client/cat.html",context)


def sp(request):
	cat=request.POST.get('Category')
	category=models.Category.objects.all()
	projects=models.Projects.objects.raw("select * from projects as p join registration as r on r.reg_id=p.fk_reg_id join category as c on c.cat_id=p.fk_cat_id where c.cat_id=%s",[cat])
	context={
	'category':category,
	'projects':projects,
	}
	return render(request,"client/cat.html",context)


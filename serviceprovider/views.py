from django.shortcuts import render,redirect
from django.http import HttpResponse
from final import models
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
 

# Create your views here.
def servicehome(request):
	return render(request,"servicep/service.html")

def myprofile(request):
	pname=request.session['semail']
	profile=models.Registration.objects.get(email_id=pname)
	context= {
	'profile': profile
	}
	return render(request,"servicep/profile.html",context)
	# return HttpResponse(pname)

def editprofile(request,reg_id):
	profile=models.Registration.objects.get(reg_id=reg_id)
	context= {
	'profile': profile
	}
	return render(request,"servicep/editprofile.html",context)

def update_profile(request):
	reg_id = request.POST['reg_id']
	name=request.POST['name']
	address=request.POST['address']
	state=request.POST['state']
	district=request.POST['district']
	city=request.POST['city']
	phonenumber=request.POST['pnumber']
	new=models.Registration.objects.get(reg_id=reg_id)
	new.reg_name=name
	new.address=address
	new.state=state
	new.district=district
	new.city=city
	new.phone_number=phonenumber
	new.save()
	return redirect("myprofile")

def change_pass_servicep(request):
	return render(request,"servicep/change_pass.html")

def update_pass(request):
	npass=request.POST['newpsw']
	cpass=request.POST['confpsw']
	uname=request.session['semail']
	if npass==cpass:
		log=models.Login.objects.get(username=uname)
		log.password=npass
		log.save()
		return redirect("myprofile")
	else:
		return redirect("change_pass")

def logoutofsp(request):
	return render(request,"newhome/index.html")

def payment(request):
    package=models.Package.objects.all()
    context= {
    'packlist':package
    }
    return render(request,"servicep/payment.html",context)

def pay(request):
	name=request.POST['name']
	card_no=request.POST['card_no']
	acc_det=models.AccountDetails.objects.get(acc_name=name,card_no=card_no)

	if acc_det:
		package=request.POST.get('Package')
		amount=request.POST.get('rate')
		payment=models.ServiceproviderdetailsPayment.objects.create(
          se_email=request.session['semail'],
          fk_pack_id=package,
          amount=amount,
          status='paid'
          )
		payment.save()
		models.Registration.objects.filter(email_id=request.session.get('semail')).update(paid_status='paid')
		return redirect("servicehome")



def addproject(request): 
	categories = models.Category.objects.all()
	cat_name=request.POST.get('category')
	se_email=request.session['semail']
	reg_data=models.Registration.objects.get(email_id=se_email)
	reg_id=reg_data.reg_id
	projects=models.Projects.objects.raw("SELECT * FROM projects AS p JOIN category AS c ON p.fk_cat_id = c.cat_id where p.fk_reg_id =%s",[reg_id])
	
	
	# return HttpResponse(categories)
	context = {
	'slist': projects,
	'categories': categories,
	}
	return render(request, "servicep/project.html", context)

def saveproject(request):
	
	se_email=request.session['semail']
	reg_data=models.Registration.objects.get(email_id=se_email)
	reg_id=reg_data.reg_id
	category_id = request.POST['category']
	title=request.POST['title']

	if request.method == 'POST' and request.FILES['image']:
		picture=request.FILES['image']
		fss = FileSystemStorage()
		file = fss.save(picture.name,picture)
		# category = models.Category.objects.get(cat_id=category_id)
		# category_name = category.cat_name
		sproject =models.Projects(proj_title=title,fk_reg_id=reg_id,fk_cat_id=category_id,image_name=file)
		# return HttpResponse(category_name)
		sproject.save()
		return redirect("addproject")
	# 	messages.success(request,'saved successfully!!!')
	# else:
	# 	messages.error("Please select a file")

	# 	return redirect("addproject")

def editproject(request,proj_id):

	project=models.Projects.objects.get(pk=proj_id)
	categories = models.Category.objects.all()
	context={
	'project': project,
	'categories': categories
	}
	return render(request,"servicep/editproject.html",context)
	# return HttpResponse('done')

def update_project(request):
	proj_id=request.POST['proj_id']
	category=request.POST['category']
	title=request.POST['title']
	# image=request.FILES.get('image')

	project=models.Projects.objects.get(pk=proj_id)
	project.fk_cat_id=category
	project.proj_title=title
	# project.image_name=image.name
	project.save()
	return redirect("addproject")

def change_image(request,proj_id):
	project=models.Projects.objects.get(pk=proj_id)
	context={
	'project':project
	}
	return render(request,"servicep/change_image.html",context)

def editimage(request):
	proj_id=request.POST.get('proj_id')
	image=request.FILES.get('image')
	project=models.Projects.objects.get(pk=proj_id)
	project.image_name=image.name
	project.save()
	return redirect("addproject")

def delete_project(request,proj_id):
	d_data=models.Projects.objects.get(proj_id=proj_id)
	d_data.delete()
	return redirect("addproject")





def portfolio(request,proj_id):

	portfolios = models.Portfolio.objects.filter(fk_prj_id=proj_id) 
	
	project=models.Projects.objects.get(pk=proj_id)
	# status = 'paid'
	# new_payment =models.ServiceproviderdetailsPayment(status=status)

	context = {
	'fk_prj_id': project.proj_id,
	'status': 'inactive',
	'slist': portfolios,
    }
	return render(request,"servicep/portfolio.html",context)

def save_portfolio(request):
	status=request.POST.get('status')
	name=request.POST['name']
	description=request.POST['description']
	fk_prj_id = request.POST['fk_prj_id']
	n_portfolio=models.Portfolio(p_name=name,p_desc=description,fk_prj_id=fk_prj_id,status='inactive')
	n_portfolio.save()

	# n_project=models.Projects()
	# return HttpResponse(status)
	return redirect("portfolio",proj_id=fk_prj_id)

def edit_portfolio(request,portfolio_id):
	portfolio=models.Portfolio.objects.get(pk=portfolio_id)
	context={
	'portfolio':portfolio,
	'portfolio_id': portfolio_id,
	}
	return render(request,"servicep/editportfolio.html",context)

def update_portfolio(request):
	portfolio_id=request.POST['portfolio_id']
	name=request.POST['name']
	description=request.POST['description']
	new_portfolio=models.Portfolio.objects.get(pk=portfolio_id)
	new_portfolio.p_name=name
	new_portfolio.p_desc=description
	new_portfolio.save()
	return redirect("portfolio",proj_id=new_portfolio.fk_prj_id)


def delete_portfolio(request,portfolio_id):
	deletep=models.Portfolio.objects.get(pk=portfolio_id)
	proj_id = deletep.fk_prj_id
	deletep.delete()
	return redirect("portfolio",proj_id=proj_id)

def gallery_view(request,portfolio_id):
	portfolio=models.Portfolio.objects.get(pk=portfolio_id)
	gallery=models.Gallery.objects.filter(fk_portfolio_id=portfolio_id)
	if request.method == 'POST' and request.FILES['image']:
		picture=request.FILES['image']
		fss = FileSystemStorage()
		file = fss.save(picture.name,picture)
		gallery =models.Gallery(fk_portfolio_id=portfolio_id,image_name=file,status='inactive')
		gallery.save()
		return redirect("gallery_view", portfolio_id=portfolio_id)

	context={
	'portfolio': portfolio,
	'gallery': gallery,
	}

	return render(request,"servicep/addimage.html",context)

def deleteg(request,gallery_id):
	deleteg=models.Gallery.objects.get(pk=gallery_id)
	portfolio_id=deleteg.fk_portfolio_id
	deleteg.delete()
	return redirect("gallery_view",portfolio_id=portfolio_id)

def change_port_image(request,gallery_id):
	gallery=models.Gallery.objects.get(pk=gallery_id)
	context={
	'gallery':gallery,

	}
	return render(request,"servicep/change_port_image.html",context)

def newimage(request):
	gallery_id=request.POST.get('gallery_id')
	image=request.FILES.get('image')
	gallery=models.Gallery.objects.get(pk=gallery_id)
	gallery.image_name=image.name
	gallery.status='inactive'
	gallery.save()
	portfolio_id=gallery.fk_portfolio_id
	return redirect("gallery_view",portfolio_id=portfolio_id)

def viewreason(request,gallery_id):
	gallery=models.Gallery.objects.get(pk=gallery_id)
	context={
	'gallery':gallery
	}
	return render(request,"servicep/viewreason.html",context)

	







	





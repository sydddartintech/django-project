from django.shortcuts import render,redirect
from final import models
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.
def admin(request):
	return render(request,"admin/admin.html")

def change_pass(request):
	return render(request,"admin/change_pass.html")

def logout(request):
	return render(request,"newhome/index.html")

def update_pass(request):
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

def category(request):
	sdata=models.Category.objects.all()
	context={
	'slist':sdata
	}
	return render(request,"category/category.html",context)

def savedata(request):
	catname=request.POST['catname']
	if models.Category.objects.filter(cat_name=catname).exists():
		messages.error(request, 'Category already exists.')
	else:
		messages.success(request, 'Category added successfully.')
		sdata=models.Category(cat_name=catname)
		sdata.save()
	return redirect("category")

def edit_category(request,cat_id):
	    data = models.Category.objects.get(pk=cat_id)
	    context = {
	    'sdata':data
	    }
	    return render(request, "category/editcat.html", context)

def update_data(request):
	catname=request.POST['catname']
	cat_id=request.POST['cat_id']
	stdata=models.Category.objects.get(cat_id=cat_id)
	stdata.cat_name=catname
	stdata.save()
	return redirect("category")

def delete_data(request,cat_id):
	sdata=models.Category.objects.get(cat_id=cat_id)
	sdata.delete()
	return redirect("category")

def package(request):
	sdata=models.Package.objects.all()
	context={
	'slist':sdata
	}
	return render(request,"package/package.html",context)

def savepack(request):
  if request.method == 'POST':
  	packname = request.POST.get('packname')
  	duration = request.POST.get('duration')
  	rate = request.POST.get('rate')
  	if models.Package.objects.filter(pack_name=packname).exists():
  		messages.error(request, 'Package already exists.')
  	else:
  		messages.success(request, 'Package added successfully.')
  		sdata=models.Package(pack_name=packname,pack_duration=duration,rate=rate)
  		sdata.save()
  		return redirect("package")
  return redirect("package")

def editpack(request,pid):
	data = models.Package.objects.get(pk=pid)
	context = {
	'sdata':data
	}
	return render(request, "package/editpack.html", context)

def updatepack(request):
	packname=request.POST['packname']
	duration=request.POST['duration']
	rate=request.POST['rate']
	pid=request.POST['pid']
	stdata=models.Package.objects.get(pid=pid)
	stdata.pack_name=packname
	stdata.pack_duration=duration
	stdata.rate=rate
	stdata.save()
	return redirect("package")

def deletepack(request,pid):
	sdata=models.Package.objects.get(pid=pid)
	sdata.delete()
	return redirect("package")

def serviceprovider(request):
	return render(request,"serviceprovider/service.html")

def search(request):
	inactive=request.POST['status']
	new=models.Registration.objects.raw("select * from registration r inner join login l on r.email_id=l.username where l.user_type='Service_provider' and l.status=%s",[inactive])
	context={
	'inactive':new
	}
	return render(request,"serviceprovider/service.html",context)

def approve(request,reg_id):
	data=models.Registration.objects.get(reg_id=reg_id)
	username=data.email_id
	log=models.Login.objects.get(username=username)
	log.status='active'
	log.save()
	# return HttpResponse(username)
	# data.status='active'
	# data.save()
	return redirect("serviceprovider")

def reject(request,reg_id):
	data=models.Registration.objects.get(reg_id=reg_id)
	username=data.email_id
	log=models.Login.objects.get(username=username)
	log.status='rejected'
	log.save()
	return redirect("serviceprovider")

# for viewing portfolio request

def portfolio_admin(request):
	# portfolios = models.Portfolio.objects.all()
	# context = {
	# 'slist': portfolios,
	# }
	return render(request,"portfolio_admin/portfolio_admin.html")

def search_port(request):
	status=request.POST['status']
	new=models.Portfolio.objects.raw("select * from projects as p join portfolio as o on o.fk_prj_id=p.proj_id where o.status=%s",[status])
	# return HttpResponse(new)
	context={
	'slist':new
	}
	return render(request,"portfolio_admin/portfolio_admin.html",context)

def approve_port_request(request,portfolio_id):
	new=models.Portfolio.objects.get(portfolio_id=portfolio_id)
	new.status='active'
	new.save()
	return redirect("portfolio_admin")
def reject_port_request(request,portfolio_id):
	new=models.Portfolio.objects.get(portfolio_id=portfolio_id)
	new.status='rejected'
	new.save()
	return redirect("portfolio_admin")

def view_details(request,proj_id):
	# project=models.Projects.objects.get(pk=proj_id)
	registrations=models.Portfolio.objects.raw("SELECT * FROM portfolio as p JOIN projects as pr ON p.fk_prj_id = pr.proj_id JOIN registration AS r ON pr.fk_reg_id = r.reg_id WHERE p.portfolio_id =%s",[proj_id])
	portfolio=models.Portfolio.objects.get(portfolio_id=proj_id)
	context={
	# 'project': project,
	'registrations': registrations,
	'portfolio':portfolio
	}
	return render(request,"portfolio_admin/view_details.html",context)

def view_gallery(request,portfolio_id): 
	portfolio=models.Portfolio.objects.get(pk=portfolio_id)
	gallery =models.Gallery.objects.raw("SELECT * FROM gallery as g JOIN portfolio as p ON g.fk_portfolio_id = p.portfolio_id WHERE p.portfolio_id = %s",[portfolio_id])
	context={
	'portfolio': portfolio,
	'gallery': gallery,
	}
	return render(request,"portfolio_admin/view_gallery.html",context)

def approve_gallery(request,gallery_id):
	new=models.Gallery.objects.get(gallery_id=gallery_id)
	new.status='active'
	new.save()
	return redirect("portfolio_admin")
def reject_gallery(request,gallery_id):
	new=models.Gallery.objects.get(gallery_id=gallery_id)
	new.status='rejected'
	new.save()
	return redirect("portfolio_admin")


 # to the reason page
def reason(request,gallery_id):
	gallery=models.Gallery.objects.get(pk=gallery_id)
	gid=gallery.gallery_id 
	context={
	'gallery_id':gid,
	}	 
	return render(request,"portfolio_admin/reason.html",context)
def givereason(request):
	gallery_id=request.POST.get('gallery_id')
	reason=request.POST.get('reason')
	gallery=models.Gallery.objects.get(gallery_id=gallery_id)
	gallery.reason=reason
	gallery.save()
	return redirect("portfolio_admin")


	











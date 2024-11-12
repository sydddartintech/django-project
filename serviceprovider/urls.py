from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
path('servicehome/', views.servicehome, name='servicehome'),
path('myprofile/', views.myprofile, name='myprofile'),
path('editprofile/<int:reg_id>/', views.editprofile, name='editprofile'),
path('update_profile/', views.update_profile, name='update_profile'),
path('change_pass_servicep/', views.change_pass_servicep, name='change_pass_servicep'),
path('update_pass/', views.update_pass, name='update_pass'),
path('payment/', views.payment, name='payment'),
path('logoutofsp/', views.logoutofsp, name='logoutofsp'),
path('pay/', views.pay, name='pay'),

path('addproject/', views.addproject, name='addproject'),
path('saveproject/', views.saveproject, name='saveproject'),
path('editproject/<int:proj_id>/', views.editproject, name='editproject'),
path('update_project/', views.update_project, name='update_project'),
path('change_image/<int:proj_id>/', views.change_image, name='change_image'),
path('editimage/', views.editimage, name='editimage'),

path('delete_project/<int:proj_id>/', views.delete_project, name='delete_project'),


path('portfolio/<int:proj_id>/', views.portfolio, name='portfolio'),
path('save_portfolio/', views.save_portfolio, name='save_portfolio'),
path('editportfolio/<int:portfolio_id>/', views.edit_portfolio, name='edit_portfolio'),
path('update_portfolio/', views.update_portfolio, name='update_portfolio'),
path('delete_portfolio/<int:portfolio_id>/', views.delete_portfolio, name='delete_portfolio'),
path('gallery_view/<int:portfolio_id>/', views.gallery_view, name='gallery_view'),
path('deleteg/<int:gallery_id>/', views.deleteg, name='deleteg'),
path('change_port_image/<int:gallery_id>/', views.change_port_image, name='change_port_image'),
path('newimage/', views.newimage, name='newimage'),
path('viewreason/<int:gallery_id>/', views.viewreason, name='viewreason'),



] 
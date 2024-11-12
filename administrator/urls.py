from django.contrib import admin
from django.urls import path,include
from .import views



urlpatterns = [
path('admin/', views.admin, name='admin'),
path('change_pass/', views.change_pass, name='change_pass'),
path('categories/', views.category, name='category'),
path('savedata/', views.savedata, name='savedata'),
path('edit/<int:cat_id>/', views.edit_category, name='edit_category'),
path('update_data/', views.update_data, name='update_data'),
path('delete/<int:cat_id>/', views.delete_data, name='delete_data'),
path('package/',views.package,name='package'),
path('savepack/',views.savepack,name='savepack'),
path('editpack/<int:pid>/', views.editpack, name='editpack'),
path('updatepack/',views.updatepack,name='updatepack'),
path('deletepack/<int:pid>/', views.deletepack, name='deletepack'),
path('serviceprovider/', views.serviceprovider, name='serviceprovider'),
path('search/',views.search,name='search'),
path('approve/<int:reg_id>/', views.approve, name='approve'), 
path('reject/<int:reg_id>/', views.reject, name='reject'),
path('update_pass/',views.update_pass, name='update_pass'),
path('portfolio_admin/',views.portfolio_admin, name='portfolio_admin'),
path('search_port/',views.search_port, name='search_port'),
path('approve_port_request/<int:portfolio_id>/', views.approve_port_request, name='approve_port_request'), 
path('reject_port_request/<int:portfolio_id>/', views.reject_port_request, name='reject_port_request'),
path('view_details/<int:proj_id>/', views.view_details, name='view_details'),
path('view_gallery/<int:portfolio_id>/', views.view_gallery, name='view_gallery'),
path('approve_gallery/<int:gallery_id>/', views.approve_gallery, name='approve_gallery'), 
path('reject_gallery/<int:gallery_id>/', views.reject_gallery, name='reject_gallery'),
path('logout/', views.logout, name='logout'),
path('reason/<int:gallery_id>/', views.reason, name='reason'),
path('givereason/', views.givereason, name='givereason'),











]
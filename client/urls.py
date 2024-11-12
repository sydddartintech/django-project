from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
path('clienthome', views.clienthome, name='clienthome'),
path('change_pass_client', views.change_pass_client, name='change_pass_client'),
path('client_profile/', views.client_profile, name='client_profile'),
path('editclient/<int:reg_id>/', views.editclient, name='editclient'),
path('updateclient/', views.updateclient, name='updateclient'),
path('view_service_provider/', views.view_service_provider, name='view_service_provider'),
path('log_out_c/', views.log_out_c, name='log_out_c'),
path('profile/', views.profile, name='profile'),
path('changepsw/', views.changepsw, name='changepsw'),

# path('seeportfolio/', views.seeportfolio, name='seeportfolio'),
# path('search_sp/', views.search_sp, name='search_sp'),
path('go_to_sp/', views.go_to_sp, name='go_to_sp'),
# path('client_want_sp/', views.client_want_sp, name='client_want_sp'),
path('sp/', views.sp, name='sp'),


]
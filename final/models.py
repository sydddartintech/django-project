# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Accountdetails(models.Model):
    acc_id = models.AutoField(primary_key=True)
    acc_no = models.IntegerField()
    acc_name = models.CharField(max_length=200)
    card_no = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user_type = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'accountdetails'


class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'category'


class Gallery(models.Model):
    gallery_id = models.AutoField(primary_key=True)
    fk_portfolio_id = models.IntegerField()
    image_name = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    reason = models.TextField()

    class Meta:
        managed = False
        db_table = 'gallery'


class Login(models.Model):
    username = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    user_type = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'login'


class Package(models.Model):
    pid = models.AutoField(primary_key=True)
    pack_name = models.CharField(max_length=200)
    pack_duration = models.CharField(max_length=200)
    rate = models.FloatField()

    class Meta:
        managed = False
        db_table = 'package'


class Portfolio(models.Model):
    portfolio_id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=200)
    p_desc = models.TextField()
    fk_prj_id = models.IntegerField()
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'portfolio'


class Projects(models.Model):
    proj_id = models.AutoField(primary_key=True)
    proj_title = models.CharField(max_length=200)
    fk_cat_id = models.IntegerField()
    fk_reg_id = models.IntegerField()
    image_name = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'projects'


class Registration(models.Model):
    reg_id = models.AutoField(primary_key=True)
    reg_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    email_id = models.CharField(max_length=50)
    user_type = models.CharField(max_length=50)
    paid_status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'registration'


class Serviceproviderdetailspayment(models.Model):
    pid = models.AutoField(primary_key=True)
    se_email = models.CharField(max_length=50)
    fk_pack_id = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'serviceproviderdetailspayment'

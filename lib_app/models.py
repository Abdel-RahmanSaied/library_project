# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Author(models.Model):
    full_name = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=45, blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'author'


class Book(models.Model):
    title = models.CharField(max_length=45, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    rent_fee = models.FloatField(blank=True, null=True)
    release_year = models.DateField(blank=True, null=True)
    author = models.ForeignKey(Author, models.DO_NOTHING, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book'


class Customer(models.Model):
    full_name = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=45, blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class Employee(models.Model):
    full_name = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=45, blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    position = models.CharField(max_length=45, blank=True, null=True)
    salary = models.FloatField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class Purchases(models.Model):
    book = models.ForeignKey(Book, models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)
    purchase_date = models.DateField(blank=True, null=True)
    employee = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchases'


class Rents(models.Model):
    book = models.ForeignKey(Book, models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)
    employee = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True)
    rent_date = models.DateField(blank=True, null=True)
    return_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rents'

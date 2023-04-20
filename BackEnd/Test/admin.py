from django.contrib import admin
from django.conf.urls import  include, url
from .models import TestModel

# Register your models here.

class TestAdmin(admin.ModelAdmin):
  list = ('EmployeeName', 'EmployeeId', 'EmployeeDesignation', 'CurrentProject', 'Email', 'ContactNumber')

admin.site.register(TestModel, TestAdmin)
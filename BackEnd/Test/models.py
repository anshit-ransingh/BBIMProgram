from django.db import models

# Create your models here.

class TestModel(models.Model):
   EmployeeName = models.CharField(max_length = 50)
   EmployeeId = models.CharField(max_length = 10)
   EmployeeDesignation = models.CharField(max_length = 30)
   CurrentProject = models.CharField(max_length = 50)
   Email = models.EmailField()
   ContactNumber = models.CharField(max_length = 10)

#    def ContactNumberCheck(ContactNumber):
#       if ContactNumber.isnum():
#          return ContactNumber
#       else:
#          models

   def _str_(self):
     return self.title
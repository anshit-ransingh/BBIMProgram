from rest_framework import serializers
from .models import TestModel

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = ('id' ,'EmployeeName', 'EmployeeId', 'EmployeeDesignation', 'CurrentProject', 'Email', 'ContactNumber')
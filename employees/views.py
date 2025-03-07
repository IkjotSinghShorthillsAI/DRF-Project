from django.shortcuts import render
from rest_framework import mixins, generics
from api.serializers import EmployeeSerializer
from .models import Employee
# Create your views here.

class Employees(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    
    
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    

class EmployeeDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def get(self, request, pk):
        return self.retrieve(request,pk)
    
    def put(self, request, pk):
        return self.update(request,pk)
    
    def delete(self, request, pk):
        return self.destroy(request,pk)
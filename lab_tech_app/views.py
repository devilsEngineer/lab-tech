from django.shortcuts import render
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .models import Patient
from .serializers import PatientSerializer

class LabView(ViewSet):

    def addpatient(self, request, format=None):
        try:
            data = request.data
            data["pid"]=data['name']+data['phone']
            serializer = PatientSerializer(data=data)
            if serializer.is_valid():
                patient = Patient(**data)
                patient.save()
                response = serializer.data
                return Response(response, status=status.HTTP_200_OK)
            return Response("Add patient failed due to validation error", status=status.HTTP_400_BAD_REQUEST)
        except Exception as exp:
            return Response("Add patient failed -> " +str(exp), status=status.HTTP_400_BAD_REQUEST)

    def listall(self,request):
        try:
            serializer = PatientSerializer(Patient.objects.all(), many=True)
            response = {"Patients": serializer.data}
            return Response(response, status=status.HTTP_200_OK)
        except Exception as exp:
            return Response("Failed to fetch list-> " +str(exp), status=status.HTTP_400_BAD_REQUEST)

    def getpatient(self,request):
        try:
            name=request.query_params.get('name')
            phone=request.query_params.get('phone')
            pk=name+phone
            serializer = PatientSerializer(Patient.objects.get(**{
                'pid':pk
                }))
            Users.objects(enterpriseId=str(request.org_id)).delete()
            response_data=serializer.data
            response_data.pop('id')
            response = {"Patients": response_data}
            return Response(response, status=status.HTTP_200_OK)
        except Exception as exp:
            return Response("Failed to fetch Patient-> " +str(exp), status=status.HTTP_400_BAD_REQUEST)
    

    def deletepatient(self,request):
        try:
            name=request.query_params.get('name')
            phone=request.query_params.get('phone')
            pk=name+phone
            Patient.objects(pid=pk).delete()
            response = {"Patient Delete Successful"}
            return Response(response, status=status.HTTP_200_OK)
        except Exception as exp:
            return Response("Failed to delete Patient-> " +str(exp), status=status.HTTP_400_BAD_REQUEST)

    def updatepatient(self,request):
        try:
            data = request.data
            name=data['name']
            phone=data['phone']
            data['pid']=name+phone
            Patient.objects(pid=data['pid']).modify(**data,upsert=True)
            response = {"Patient Update Successful"}
            return Response(response, status=status.HTTP_200_OK)
        except Exception as exp:
            return Response("Failed to update Patient-> " +str(exp), status=status.HTTP_400_BAD_REQUEST)
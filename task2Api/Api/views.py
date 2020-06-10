from rest_framework import generics, permissions
from .models import Company
from .seializers import CompanySerializers

class CompanyList(generics.ListCreateAPIView):
    queryset            = Company.objects.all()
    serializer_class    =  CompanySerializers
    permission_classes =  (permissions.AllowAny, )
    
class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset            = Company.objects.all()
    serializer_class    = CompanySerializers
    lookup_field        = 'pk'
    permission_classes = (permissions.AllowAny, )


# from django.shortcuts import render
# from django.http import HttpResponse
# from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status


# class CompanyList(APIView): 
#     def get(self, request):
#         company = Company.objects.all()
#         serializer = CompanySerializers(company, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = CompanySerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class CompanyDetail(APIView):

#     def get(self, request, pk):
#         company = Company.objects.get(id=pk)
#         serializer = CompanySerializers(company)
#         return Response(serializer.data)

#     def delete(self, request, pk):
#         company = Company.objects.get(id=pk)
#         company.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     def put(self, request, pk):
#         company = Company.objects.get(id=pk)
#         serializer = CompanySerializers(company, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
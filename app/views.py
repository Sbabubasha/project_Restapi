from django.shortcuts import render

# Create your views here.
from app.models import *
from app.serializers import *
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response


class Product_crud(ViewSet):
    def list(self,request):
        plo=Product.objects.all()
        pso=Product_cat_serial(plo,many=True)
        return Response(pso.data)
    
    def create(self,request):
        sod=Product_cat_serial(data=request.data)
        if sod.is_valid():
            sod.save()
            return Response({'success':'data is created'})
        return Response({'Fail':'data is not created'})

    def retrieve(self,request,pk):
        rdo=Product.objects.get(pk=pk)
        Pqo=Product_cat_serial(rdo)
        return Response(Pqo.data)
    
    def update(self,request,pk):
        puo=Product.objects.get(pk=pk)
        spo=Product_cat_serial(puo,data=request.data)
        if spo.is_valid():
            spo.save()
            return Response({'update':'data is update is done'})
        return Response({'nUpdate':'data is not update'})
    def partial_update(self,request,pk):
        puo=Product.objects.get(pk=pk)
        spo=Product_cat_serial(puo,data=request.data,partial=True)
        if spo.is_valid():
            spo.save()
            return Response({'update':'data is update is done'})
        return Response({'nUpdate':'data is not update'})
    def destroy(self,request,pk):
        Product_cat_serial.objects.get(pk=pk)
        return Response

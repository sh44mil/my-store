from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Products
from api.serializers import ProductSerializer

class ProductView(APIView):
     
    def get(self,request,*args,**kw) :

        qs = Products.objects.all()

        serializer = ProductSerializer()

        return Response(data = serializer.data)
    

    def post (self,request,*args,**kw):

        serializer = ProductSerializer( data = request.data )
        
        if serializer.is_valid():
            
            print(serializer.validated_data)
            Products.objects.create(**serializer.validated_data)

            return Response (data= serializer.data)
        
        else:
             return Response(data=serializer.errors)
    
class ProductDetailsView(APIView):
    
    def get(self,request,*args,**kw):

        return Response (data='details of product')
    
    def put (self,request,*args,**kw):
        
        return Response (data= "item deleted")
    
    def delete(self,request,*args,**kw):

        return Response (data='item successfully deleted')
    

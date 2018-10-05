from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .models import producto
from .serializers import ProductoSerializer
from rest_framework import status
# Create your views here.


from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny, ))
def producto_vista(request):
	if request.method == 'GET':
		serializer = ProductoSerializer(producto.objects.all(), many=True)
		return Response(serializer.data)
	elif request.method == 'POST':
	    data = JSONParser().parse(request)
	    serializer = ProductoSerializer(data=data)
	    if serializer.is_valid():
	        serializer.save()
	        return Response(serializer.data, status=status.HTTP_201_CREATED)
	    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)	
  
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny, ))
def producto_vista_detalle(request, pk):
    if request.method == 'GET':
        serializer = ProductoSerializer(producto.objects.get(pk=pk))
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(producto.objects.get(pk=pk ), data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        producto.objects.get(pk=pk ).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
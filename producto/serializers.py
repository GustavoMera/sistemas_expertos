from rest_framework import serializers
from producto.models import producto
from .models import producto


class ProductoSerializer(serializers.ModelSerializer):
	class Meta:
		model = producto
		fields = '__all__'
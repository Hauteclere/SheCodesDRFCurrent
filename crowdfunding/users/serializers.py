from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.Serializer):
	id = serializers.ReadOnlyField()
	username = serializers.CharField(max_length=200)
	email=serializers.CharField(max_length=200)
	password=serializers.CharField(write_only = True)
	
	def create(self, validated_data):
		password = validated_data.pop('password')		
		user =  CustomUser.objects.create(**validated_data)
		user.set_password(password)
		user.save()
		return user
from django.contrib.auth import get_user_model, login, logout
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProfileSerializer
from rest_framework import permissions, status
from .validations import custom_validation, validate_email, validate_password
from .models import Profile

#<-----------------------------Old_View----------------------------------->
# class UserRegister(APIView):
# 	def post(self, request):
# 		clean_data = custom_validation(request.data)
# 		serializer = UserRegisterSerializer(data=clean_data)
# 		if serializer.is_valid(raise_exception=True):
# 			user = serializer.create(clean_data)
# 			if user:
# 				return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(status=status.HTTP_400_BAD_REQUEST)


# class UserLogin(APIView):
	
# 	def post(self, request):
# 		data = request.data
# 		assert validate_email(data)
# 		assert validate_password(data)
# 		serializer = UserLoginSerializer(data=data)
# 		if serializer.is_valid(raise_exception=True):
# 			user = serializer.check_user(data)
# 			login(request, user)
# 			return Response(serializer.data, status=status.HTTP_200_OK)


# class UserLogout(APIView):
# 	permission_classes = (permissions.AllowAny,)
# 	authentication_classes = ()
# 	def post(self, request):
# 		logout(request)
# 		return Response(status=status.HTTP_200_OK)

#<--------------------------------------End------------------------------------->

#<------------------------------------NewCode----------------------------------->

class UserView(APIView):
	authentication_classes=[TokenAuthentication]
	permission_classes=[IsAuthenticated]
	
	def get(self, request, pk=None,format=None):
		id = pk
		if id is not None:
			data_retrive = Profile.objects.get(pk=id)
			serializer = ProfileSerializer(data_retrive)
			return Response({'user': serializer.data}, status=status.HTTP_200_OK)
			
		data_retrive = Profile.objects.all()
		serializer = ProfileSerializer(data_retrive, many=True)
		print(serializer.data)
		return Response({'user': serializer.data}, status=status.HTTP_200_OK)

	def post(self, request, format=None):
		serializer = ProfileSerializer(data=request.data)
		if serializer.is_valid:
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
	def put(self, request, pk, format=None):
		id = pk
		data_retrive = Profile.objects.get(pk=id)
		serializer = ProfileSerializer(data_retrive,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'Complete Data Updated'})
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
	
	def patch(self, request, pk, format=None):
		id = pk
		data_retrive = Profile.objects.get(pk=id)
		serializer = ProfileSerializer(data_retrive, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'Partial data updated'})
		return Response(serializer.error)
	
	def delete(self, request, pk, format=None):
		id=pk
		data_retrive = Profile.objects.get(pk=id)
		data_retrive.delete()
		return Response({'msg':'Data Deleted'})
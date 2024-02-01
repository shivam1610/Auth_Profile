from django.contrib.auth import get_user_model, login, logout
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProfileSerializer,UserSerializer
from rest_framework import permissions, status
# from .validations import custom_validation, validate_email, validate_password
from .models import Profile,User

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

#<------------------------------------Code with CRUD Tested----------------------------------->

# class UserView(APIView):

# 	# authentication_classes=[TokenAuthentication]
# 	# permission_classes=[IsAuthenticated]
	
# 	"""
# 	This code is excuted once the user is authanticated to get data foe which he authorised
# 	"""
# 	def get(self, request, pk=None,format=None):
# 		id = pk
# 		if id is not None:
# 			data_retrive_profile = Profile.objects.get(pk=id)
# 			data_retive_user = User.objects.get(pk=id)
# 			serializer_profile = ProfileSerializer(data_retrive_profile)
# 			serializer_user = UserSerializer(data_retive_user)
# 			return Response({'profile': serializer_profile.data, 'user':serializer_user.data}, status=status.HTTP_200_OK)
			
# 		data_retrive_profile = Profile.objects.all()
# 		data_retive_user = User.objects.all()
# 		serializer_profile = ProfileSerializer(data_retrive_profile, many=True)
# 		serializer_user = UserSerializer(data_retive_user, many=True)
# 		return Response({'profile': serializer_profile.data, 'user':serializer_user.data}, status=status.HTTP_200_OK)

# 	#Not needed as profile is created instantly
# 	# """
# 	# This code is to create new data
# 	# """
# 	# def post(self, request, format=None):
# 	# 	serializer = ProfileSerializer(data=request.data)
# 	# 	if serializer.is_valid:
# 	# 		serializer.save()
# 	# 		return Response(serializer.data, status=status.HTTP_201_CREATED)
# 	# 	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
# 	"""
# 	This code is to change whole data that is exciting on profile
# 	"""
# 	def put(self, request, pk, format=None):
# 		id = pk
# 		data_retrive = Profile.objects.get(pk=id)
# 		serializer = ProfileSerializer(data_retrive,data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response({'msg':'Complete Data Updated'})
# 		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
	
# 	"""
# 	This code is to change pritial data profile
# 	"""
# 	def patch(self, request, pk, format=None):
# 		id = pk
# 		data_retrive = Profile.objects.get(pk=id)
# 		serializer = ProfileSerializer(data_retrive, data=request.data, partial=True)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response({'msg':'Partial data updated'})
# 		return Response(serializer.error)
	
# 	"""
# 	This code is to delete profile data from data base
# 	"""
# 	def delete(self, request, pk, format=None):
# 		id=pk
# 		data_retrive = Profile.objects.get(pk=id)
# 		data_retrive.delete()
# 		return Response({'msg':'Data Deleted'})

#<----------------------------------END----------------------------------------------------->

class UserProfileView(APIView):
	# authentication_classes=[TokenAuthentication]
	# permission_classes=[IsAuthenticated]
	"""
	This code is excuted once the user is authanticated to get data foe which he authorised
	"""
	def get(self, request, pk=None,format=None):
		id = pk
		if id is not None:
			data_retrive_profile = Profile.objects.get(pk=id)
			data_retive_user = User.objects.get(pk=id)
			serializer_profile = ProfileSerializer(data_retrive_profile)
			serializer_user = UserSerializer(data_retive_user)
			return Response({'profile': serializer_profile.data, 'user':serializer_user.data}, status=status.HTTP_200_OK)
			
		# data_retrive_profile = Profile.objects.all()
		# data_retive_user = User.objects.all()
		# serializer_profile = ProfileSerializer(data_retrive_profile, many=True)
		# serializer_user = UserSerializer(data_retive_user, many=True)
		return Response({'user':serializer_user.data}, status=status.HTTP_200_OK)

class CompleteProfile(APIView):
	# authentication_classes=[TokenAuthentication]
	# permission_classes=[IsAuthenticated]
	"""
	This code is to change whole data that is exciting on profile
	"""
	def put(self, request, pk, format=None):
		id = pk
		data_retrive = Profile.objects.get(pk=id)
		serializer = ProfileSerializer(data_retrive,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'Complete Data Updated'})
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class EditProfile(APIView):
	# authentication_classes=[TokenAuthentication]
	# permission_classes=[IsAuthenticated]
	"""
	This code is to change pritial data profile
	"""
	def patch(self, request, pk, format=None):
		id = pk
		data_retrive = Profile.objects.get(pk=id)
		serializer = ProfileSerializer(data_retrive, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'Partial data updated'})
		return Response(serializer.error)

class DeleteProfile(APIView):
	# authentication_classes=[TokenAuthentication]
	# permission_classes=[IsAuthenticated]
	"""
	This code is to delete profile data from data base
	"""
	def delete(self, request, pk, format=None):
		id=pk
		data_retrive = Profile.objects.get(pk=id)
		data_retrive.delete()
		return Response({'msg':'Data Deleted'})
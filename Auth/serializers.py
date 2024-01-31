from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model, authenticate
from .models import Profile


#<-----------------------------Old Code-------------------------------------->
# UserModel = get_user_model()

# class UserRegisterSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = UserModel
# 		fields = '__all__'
# 	def create(self, clean_data):  
# 		user_obj = UserModel.objects.create_user(email=clean_data['email'], password=clean_data['password'])
# 		user_obj.username = clean_data['username']
# 		user_obj.save()
# 		return user_obj

# class UserLoginSerializer(serializers.Serializer):
# 	email = serializers.EmailField()
# 	password = serializers.CharField()
# 	##
# 	def check_user(self, clean_data):
# 		user = authenticate(username=clean_data['email'], password=clean_data['password'])
# 		if not user:
# 			raise ValidationError('user not found')
# 		return         

# class UserSerializer(serializers.ModelSerializer):
# 	user = serializers.RelatedField(many=True,read_only=True)
# 	class Meta:
# 		model: AppUser
# 		fields = ('email', 'username')
  
# class ProfileSerializer(serializers.ModelSerializer):
# 	user = serializers.RelatedField(many=True, read_only=True)
# 	class Meta:
# 		model = Profile
# 		fields = ('user','image','location','cv','certificates','paydetails','Leave')
 
#<-----------------------------------NEw Code----------------------------------------------->

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('Name','Phone','Location','Leave')

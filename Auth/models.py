from django.db import models
# from django.contrib.auth.base_user import BaseUserManager
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import User

#<--------------------------Old Code----------------------------->
# class AppUserManager(BaseUserManager):
# 	def create_user(self, email, password=None):
# 		if not email:
# 			raise ValueError('An email is required.')
# 		if not password:
# 			raise ValueError('A password is required.')
# 		email = self.normalize_email(email)
# 		user = self.model(email=email)
# 		user.set_password(password)
# 		user.save()
# 		return user
# 	def create_superuser(self, email, password=None):
# 		if not email:
# 			raise ValueError('An email is required.')
# 		if not password:
# 			raise ValueError('A password is required.')
# 		user = self.create_user(email,password=password)
# 		user.is_admin = True
# 		user.is_active = True
# 		user.is_superuser = True
# 		user.is_staff = True
# 		user.save()
# 		return user

# class AppUser(AbstractBaseUser, PermissionsMixin):
# 	is_staff = models.BooleanField('staff status',default=False)
# 	is_active = models.BooleanField(default=True)
# 	is_admin = models.BooleanField(default=False)
# 	user_id = models.AutoField(primary_key=True)
# 	email = models.EmailField(max_length=50, unique=True)
# 	username = models.CharField(max_length=50)
# 	USERNAME_FIELD = 'email'
# 	REQUIRED_FIELDS = ['password']

# 	objects = AppUserManager()


# Profile Model
#class Profile(models.Model):
	#user = models.OneToOneField(AppUser,on_delete=models.CASCADE, related_name='user')
	#image = models.ImageField(default='profilepic.jpg',upload_to='profile_pictures')
	#location = models.CharField(default='No Location assigned',max_length=100)
	# cv = models.FileField(default='No Location assigned',upload_to='profile_cv')
	# certificates = models.FileField(default='No Location assigned',upload_to='certificates')
	# paydetails = models.ImageField(default='No Location assigned',upload_to='paydetails')
	#Leave = models.IntegerField(default=0)

	# def __str__(self):
	# 	return self.user.username 

#<--------------------------End----------------------------------->

#<-------------------------New------------------------------------->

#Profile Model
class Profile(models.Model):
	User = models.OneToOneField(User, on_delete=models.CASCADE)
	Name = models.CharField(max_length=100)
	Phone = models.IntegerField(default=0)
	Location = models.CharField(max_length=100)
	Leave = models.IntegerField(default=0)
	
	def __str__(self):
		return self.Name


from django.urls import path
from . import views
from .token_auth import CustomAuthToken

urlpatterns = [
    #<-------------------------OldURl-------------------------------->
	# path('register', views.UserRegister.as_view(), name='register'),
	# path('login', views.UserLogin.as_view(), name='login'),
	# path('logout', views.UserLogout.as_view(), name='logout'),
    #<-------------------------End----------------------------------->
    
	# path('users', views.UserView.as_view(), name='user'),
    path('users/<int:pk>/', views.UserProfileView.as_view(), name='each_user'),
    path('profilecomplete/<int:pk>/', views.CompleteProfile.as_view(), name='complete_profile'),
    path('editprofile/<int:pk>/', views.EditProfile.as_view(), name='edited_profile'),
    path('delete/<int:pk>/', views.DeleteProfile.as_view(), name='delete_profile'),
    path('payslipsview/<int:pk>/',views.PaySlipsView.as_view(),name='payslip'),
    path('stackcertifiacte/<int:pk>/', views.StackCertificateView.as_view(), name='stackcertificate'),
    path('resumeview/<int:pk>/', views.ResumeView.as_view(), name='stackcertificate'),
    path('login/', CustomAuthToken.as_view(), name = 'login_createuser')
] 
from django.urls import path
from . import views

urlpatterns = [
    #<-------------------------OldURl-------------------------------->
	# path('register', views.UserRegister.as_view(), name='register'),
	# path('login', views.UserLogin.as_view(), name='login'),
	# path('logout', views.UserLogout.as_view(), name='logout'),
    #<-------------------------End----------------------------------->
    
	path('users', views.UserView.as_view(), name='user'),
    path('users/<int:pk>/', views.UserView.as_view(), name='each_user'),
] 
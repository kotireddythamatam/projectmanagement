####################### django #########################
from django.urls import path, include

####################### django #########################
from rest_framework import routers

####################### user_app #########################
from .views import (
	UserAPI, LoginAPI
)


router = routers.DefaultRouter()
router.register('users', UserAPI, basename='users')

urlpatterns = [
	path('', include(router.urls)),

	path('login/', LoginAPI.as_view(), name="login")
	

]

	# path('password-reset-link-verify/<str:uidb64>/<str:token>/',
	# 	PasswordResetLinkVerifyAPI.as_view(), name="password-reset-link-verify")
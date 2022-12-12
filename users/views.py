######################## django #########################
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, smart_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from rest_framework_jwt.settings import api_settings

######################## django #########################
from rest_framework import viewsets, status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

######################## users #########################
from .serializers import (
	UserSerializer,
)
from .models import User

######################## common #########################
from common.utils import (
	current_site_details, get_protocol_type, send_basic_mail
)


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class UserAPI(viewsets.ModelViewSet):
	"""
		User crud operations will done
	"""
	queryset = User.objects.filter(is_active=True)
	serializer_class = UserSerializer

	def list(self, request, *args, **kwargs):
		return super().list(request, *args, **kwargs)

	def create(self, request, *args, **kwargs):
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(data={'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)
		return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def retive(self, request, *args, **kwargs):
		return super().retive(request, *args, **kwargs)

	def update(self, request, *args, **kwargs):
		return super().update(request, *args, **kwargs)

	def destroy(self, request, *args, **kwargs):
		return super().destroy(request, *args, **kwargs)


class LoginAPI(APIView):
    permission_classes = (AllowAny,)
    
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            token = jwt_encode_handler(jwt_payload_handler(user))
            return Response({'email': user.email, 'token': token}, status=status.HTTP_200_OK)                           
        return Response(status=status.HTTP_401_UNAUTHORIZED)
















































# class PasswordResetAPI(viewsets.ModelViewSet):
# 	serializer_class = PasswordResetEmailSerializer
# 	queryset = User.objects.all()
# 	# http_method_names = ['post', 'patch']

# 	def get_serializer_class(self):
# 		if self.action == "update":
# 			return PasswordResetSerializer
# 		return PasswordResetEmailSerializer

# 	def create(self, request, *args, **kwargs):
# 		serializer = self.serializer_class(data=request.data)
# 		# print(serializer.get_initial())
# 		serializer.is_valid(raise_exception=True)
# 		email = request.data.get('email')
# 		user_obj = User.objects.get(email=email)
# 		uidb64 = urlsafe_base64_encode(smart_bytes(user_obj.id))
# 		token = PasswordResetTokenGenerator().make_token(user_obj)
# 		domain = current_site_details(request)
# 		redirect_url = reverse('password-reset-link-verify', kwargs={"uidb64": uidb64, "token": token})
# 		protocol_type = get_protocol_type(request)
# 		url = "{0}{1}{2}".format(protocol_type, domain, redirect_url)
# 		subject = "Password Reset Link"
# 		body='''Hello {}, \n Plese click on the below link to reset password. \n
# 			link: {}'''.format(user_obj.get_full_name(), url)
# 		to_email = [user_obj.email]
# 		send_basic_mail(subject, body, to_email)
# 		return Response({'Password reset link shared to the email'}, status=status.HTTP_200_OK)

# 	def update(self, request, *args, **kwargs):
# 		serializer = self.serializer_class(data=request.data)
# 		serializer.is_valid(raise_exception=True)
# 		return Response({"message": "Password updated successfully."})

# 	# def perform_update(self, serializer):
# 	# 	return super().perform_update(serializer)


# class PasswordResetLinkVerifyAPI(APIView):

# 	def get(self, request, uidb64, token):
# 		uid = smart_str(urlsafe_base64_decode(uidb64))
# 		user_obj = User.objects.get(id=uid)
# 		if PasswordResetTokenGenerator().check_token(user_obj, token):
# 			return HttpResponseRedirect(reverse("password-reset"))
# 		return Response({"message": "Token verification failed. Please try again later."})






















































# class RegistrationAPIView(APIView):
#     # Allow any user (authenticated or not) to hit this endpoint.
#     permission_classes = (AllowAny,)
#     serializer_class = UserSerializer

#     def post(self, request):
#         user = request.data.get('user', {})

#         # The create serializer, validate serializer, save serializer pattern
#         # below is common and you will see it a lot throughout this course and
#         # your own work later on. Get familiar with it.
#         serializer = self.serializer_class(data=user)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# class UserRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthenticated,)
#     renderer_classes = (UserJSONRenderer,)
#     serializer_class = UserSerializer

#     def retrieve(self, request, *args, **kwargs):
#         # There is nothing to validate or save here. Instead, we just want the
#         # serializer to handle turning our `User` object into something that
#         # can be JSONified and sent to the client.
#         serializer = self.serializer_class(request.user)

#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def update(self, request, *args, **kwargs):
#         serializer_data = request.data.get('user', {})

#         # Here is that serialize, validate, save pattern we talked about
#         # before.
#         serializer = self.serializer_class(
#             request.user, data=serializer_data, partial=True
#         )
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(serializer.data, status=status.HTTP_200_OK)
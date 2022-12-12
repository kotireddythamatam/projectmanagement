######################## rest_framework #########################
from rest_framework import serializers
from rest_framework.validators import ValidationError

######################## django #########################
from django.contrib.auth import password_validation

######################## rest_framework #########################
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
        User serializer
        Password should be minimum of 8 characters and maximum of 128 characters.
        Password should be write only means it won't display in response.
        Email and password are mandatory fields, fist_name, last_name optional. 
    """
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    conform_password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name', 'email',
            'password', 'conform_password',
        ]

    def validate_password(self, value):
        password_validation.validate_password(value, self.instance)
        return value 

    def create(self, validated_data):
        """
            Performs create operation on a User.
        """
        validated_data.pop('conform_password')
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """
            Performs an update operation on a User.
        """
        password = validated_data.pop('password', None)
        for key, value in validated_data.items():
            setattr(instance, key, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


































# class PasswordResetEmailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['email']

#     def validate(self, attrs):
#         email = attrs.get('email', '')
#         if not email:
#             raise ValidationError("Please provide an email!")
#         if not User.objects.filter(email=email).exists():
#             raise ValidationError("Please provide registered email")
#         return super().validate(attrs)


# class PasswordResetSerializer(serializers.Serializer):

#     password = serializers.CharField(max_length=128, min_length=8, write_only=True)
#     conform_password = serializers.CharField(max_length=128, min_length=8, write_only=True)

#     class Meta:
#         fields = ['password', 'conform_password']

#     def validate(self, attrs):
#         password = attrs.get('password')
#         if password.isdigit():
#             raise ValidationError("Password contain only digits.")
#         elif password.isalpha():
#             raise ValidationError("Password contain only alphabeticals")
#         conform_password = attrs.get('conform_password')
#         if password != conform_password:
#             raise ValidationError("Password and conform password are not matching!.")
#         return super().validate(attrs)

#     def update(self, instance, validated_data):
#         instance.set_password(validated_data.get('password'))
#         instance.save
#         return instance






















































# class UserSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = User
# 		fields = "__all__"
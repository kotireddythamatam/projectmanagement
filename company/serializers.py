######################## rest_framework #########################
from rest_framework import serializers

######################## company #########################
from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        

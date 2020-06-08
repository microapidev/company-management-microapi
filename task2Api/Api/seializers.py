from rest_framework import serializers
from .models import Company


class CompanySerializers(serializers.ModelSerializer):


    class Meta():
        model = Company
        fields = '__all__'

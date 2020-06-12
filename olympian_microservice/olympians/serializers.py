from django.utils import timezone
from rest_framework import serializers
from .models import Company
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(many=True, queryset=Company.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'company']



class CompanySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='olympians:company-detail', lookup_field='pk')
    # highlight = serializers.HyperlinkedIdentityField(view_name='olympians:company-highlight', format='html')
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Company
        fields = [
                'url',
                'pk',
                'owner',
                'company_name',
                'company_email',
                'company_address',
                'company_description',
                'company_logo',                     
        ]
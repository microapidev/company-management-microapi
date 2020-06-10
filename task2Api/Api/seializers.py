from rest_framework import serializers
from .models import Company


class CompanySerializers(serializers.ModelSerializer):
    see_detail =  serializers.HyperlinkedIdentityField(view_name='detail', lookup_field='pk' )

    class Meta():
        model = Company
        fields = (
                
                'name',
                'address',
                'phoneNumber',
                'email',
                'see_detail',
                )
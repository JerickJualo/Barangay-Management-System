from rest_framework import serializers
from .models import Resident, Household, Street, Purok

class PurokSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purok
        fields = ['id', 'number']

class StreetSerializer(serializers.ModelSerializer):
    purok = PurokSerializer(read_only=True)
    purok_id = serializers.PrimaryKeyRelatedField(
        queryset=Purok.objects.all(), source='purok', write_only=True
    )

    class Meta:
        model = Street
        fields = ['id', 'name', 'purok', 'purok_id']

class HouseholdSerializer(serializers.ModelSerializer):
    street = StreetSerializer(read_only=True)
    street_id = serializers.PrimaryKeyRelatedField(
        queryset=Street.objects.all(), source='street', write_only=True
    )
    
    class Meta:
        model = Household
        fields = ['id', 'number', 'head_of_family', 'street', 'street_id']

class ResidentSerializer(serializers.ModelSerializer):
    household = HouseholdSerializer(read_only=True)
    household_id = serializers.PrimaryKeyRelatedField(
        queryset=Household.objects.all(), source='household', write_only=True
    )
    
    class Meta:
        model = Resident
        fields = [
            'id', 'name', 'birthdate', 'sex', 'civil_status', 
            'contact_number', 'occupation', 'household', 'household_id'
        ]

from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import WifiLocation

class WifiLocationSerializer(serializers.ModelSerializer):
    added_by = serializers.ReadOnlyField(source='added_by.username')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()

    # Method to get human-readable 'created_at'
    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    # Method to get human-readable 'updated_at'
    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    # Method to determine if the request user is the owner of the object
    def get_is_owner(self, obj):
        request = self.context.get('request')
        return request.user == obj.added_by

    class Meta:
        model = WifiLocation
        fields = [
            'name', 
            'street',
            'city',
            'country',
            'postcode',
            'image', 
            'description', 
            'amenities', 
            'added_by', 
            'created_at', 
            'updated_at',
            'is_owner'
        ]

from django.contrib.gis.geos import Point
from rest_framework import serializers
from school.models import Organization, School


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = (
            'name',
            'headquarters',
            'type',
        )


class GeolocationField(serializers.Field):
    def to_internal_value(self, data):

        if not isinstance(data, dict):
            raise serializers.ValidationError("Invalid geolocation format. Please provide a dictionary.")

        latitude = data.get('latitude')
        longitude = data.get('longitude')

        if latitude is None or longitude is None:
            raise serializers.ValidationError("Latitude and longitude are required.")

        try:
            return Point(float(longitude), float(latitude))
        except (ValueError, TypeError):
            raise serializers.ValidationError("Invalid latitude or longitude values.")

    def to_representation(self, value):
        if value is None:
            return None

        return {'latitude': value.y, 'longitude': value.x}


class SchoolSerializer(serializers.ModelSerializer):
    geolocation = GeolocationField()

    class Meta:
        model = School
        fields = (
            'name',
            'branch',
            'address',
            'established_by',
            'website',
            'contact_number',
            'founded_date',
            'description',
            'logo',
            'geolocation',
        )
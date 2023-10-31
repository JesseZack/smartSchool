from rest_framework import serializers

from users.models import CustomUser, SchoolAdmin


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'email',
            'gender',
            'password',
            'profile_pic',
            'address'
        )


class SchoolAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolAdmin
        fields = (
            'first_name',
            'last_name',
            'email',
            'gender',
            'password',
            'profile_pic',
            'address',
            'primary_contact_number'
        )

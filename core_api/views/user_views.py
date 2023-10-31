from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from core_api.serializers.user_serializers import UserSerializer, SchoolAdminSerializer
from school.models import School
from users.models import CustomUser, SchoolAdmin, Staff


class UserListView(ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserDetailView(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class SchoolAdminListView(ListCreateAPIView):
    queryset = SchoolAdmin.objects.all()
    serializer_class = SchoolAdminSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SchoolAdminDetailView(RetrieveAPIView):
    queryset = SchoolAdmin.objects.all()
    serializer_class = SchoolAdminSerializer


@api_view(['POST'])
def check_in(request):
    if request.method == 'POST':
        name = request.data.get('name')
        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')

        location = Point(float(longitude), float(latitude))

        school_id = Staff.objects.get(name=name).current_school

        try:
            school_location = School.objects.get(id=school_id).location
        except School.DoesNotExist:
            return Response({'error': 'School not found'}, status=status.HTTP_404_NOT_FOUND)

        distance_to_school = location.distance(school_location)

        proximity_threshold = 100

        if distance_to_school <= proximity_threshold:
            Staff.objects.create(name=name, location=location)
            return Response({'message': 'Attendance recorded successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Staff member is too far from the school'}, status=status.HTTP_400_BAD_REQUEST)
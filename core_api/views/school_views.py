from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from core_api.serializers.school_serializer import SchoolSerializer, OrganizationSerializer
from school.models import School, Organization


class SchoolListCreateView(ListCreateAPIView):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()


class SchoolDetailView(RetrieveAPIView):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()


class OrganizationListCreateView(ListCreateAPIView):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()


class OrganizationDetailView(RetrieveAPIView):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()

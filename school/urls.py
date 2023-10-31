from django.urls import path

from core_api.views.school_views import SchoolDetailView, OrganizationDetailView, OrganizationListCreateView, \
    SchoolListCreateView

app_name = 'schools'

urlpatterns = [
    path('', SchoolListCreateView.as_view(), name='school-list'),
    path('<int:pk>/', SchoolDetailView.as_view(), name='school-detail'),
    path('orgs/', OrganizationListCreateView.as_view(), name='organizations'),
    path('org/<int:pk>/', OrganizationDetailView.as_view(), name='organization-detail')
]
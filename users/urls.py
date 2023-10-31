from django.urls import path

from core_api.views.user_views import UserListView, SchoolAdminListView, SchoolAdminDetailView, UserDetailView

app_name = 'users'

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('sch_admin/', SchoolAdminListView.as_view(), name='school-admin-list'),
    path('sch_admin/<int:pk>/', SchoolAdminDetailView.as_view(), name='school-admin-detail'),
]
from django.urls import path, include
from core_api.views.user_views import UserListView, UserDetailView, SchoolAdminListView, SchoolAdminDetailView

app_name = 'core_api'

urlpatterns = [
    path('exams/', include('exams.urls', namespace='exams')),
    path('users/', include('users.urls', namespace='users')),
    path('fees/', include('fees.urls', namespace='fees')),
    path('schools/', include('school.urls', namespace='schools')),
]

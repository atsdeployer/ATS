from ats_system.schema import schema_view
from django.urls import path
from .views import (
    ATSUserView,
    ATSUserDetailView,
    JobSeekerView,
    JobSeekerDetailView,
    OrganizationView,
    OrganizationDetailView
)

urlpatterns = [
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
    path('atsusers/', ATSUserView.as_view()),
    path('atsusers/<pk>/', ATSUserDetailView.as_view()),
    path('jobseekers/', JobSeekerView.as_view()),
    path('jobseekers/<pk>/', JobSeekerDetailView.as_view()),
    path('organizations/', OrganizationView.as_view()),
    path('organizations/<pk>/', OrganizationDetailView.as_view()),
]

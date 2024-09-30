from django.urls import path
from .views import (
    SkillView,
    SkillDetailView,
    JobSeekerSkillsView,
    JobSeekerSkillsDetailView,
    JobSeekerExperienceView,
    JobSeekerExperienceDetailView,
    CertificationView,
    CertificationDetailView,
    JobView,
    JobDetailView,
    JobApplicationView,
    JobApplicationDetailView,
    InterviewPanelAssignmentView,
    InterviewPanelAssignmentDetailView,
    JobSeekerEducationView,
    JobSeekerEducationDetailView,
)

urlpatterns = [
    # Skill URLs
    path('skills/', SkillView.as_view()),
    path('skills/<pk>/', SkillDetailView.as_view()),

    # JobSeekerSkills URLs
    path('jobseekerskills/', JobSeekerSkillsView.as_view()),
    path('jobseekerskills/<pk>/', JobSeekerSkillsDetailView.as_view()),

    # JobSeekerExperience URLs
    path('jobseekerexperiences/', JobSeekerExperienceView.as_view()),
    path('jobseekerexperiences/<pk>/', JobSeekerExperienceDetailView.as_view()),

    # Certification URLs
    path('certifications/', CertificationView.as_view()),
    path('certifications/<pk>/', CertificationDetailView.as_view()),

    # Job URLs
    path('jobs/', JobView.as_view()),
    path('jobs/<pk>/', JobDetailView.as_view()),

    # JobApplication URLs
    path('jobapplications/', JobApplicationView.as_view()),
    path('jobapplications/<pk>/', JobApplicationDetailView.as_view()),

    # InterviewPanelAssignment URLs
    path('interviewpanelassignments/', InterviewPanelAssignmentView.as_view()),
    path('interviewpanelassignments/<pk>/', InterviewPanelAssignmentDetailView.as_view()),

    # JobSeekerEducation URLs
    path('jobseekereducations/', JobSeekerEducationView.as_view()),
    path('jobseekereducations/<pk>/', JobSeekerEducationDetailView.as_view()),
]
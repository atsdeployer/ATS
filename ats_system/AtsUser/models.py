import uuid
from django.db import models
from django.conf import settings

class Organization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    info = models.JSONField()

    def __str__(self):
        return f"{self.name} (ID: {self.id})"

class ATSUser(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Manager', 'Manager'),
        ('HiringManager', 'Hiring Manager'),
        ('InterviewPanel', 'Interview Panel'),
        ('Recruiter', 'Recruiter'),
        ('JobSeeker', 'JobSeeker')
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='custom_user')
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='users')
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    password_text = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - Role: {self.role}"

    class Meta:
        permissions = [
            # Manager Permissions
            ("can_create_client", "Can create client"),
            ("can_view_client", "Can view client"),
            ("can_edit_client", "Can edit client"),
            ("can_delete_client", "Can delete client"),
            
            # Hiring Manager Permissions
            ("can_create_hiring_manager", "Can create hiring manager"),
            ("can_view_hiring_manager", "Can view hiring manager"),
            ("can_edit_hiring_manager", "Can edit hiring manager"),
            ("can_delete_hiring_manager", "Can delete hiring manager"),
            
            # Interview Panel Permissions
            ("can_create_interview_panel", "Can create interview panel"),
            ("can_view_interview_panel", "Can view interview panel"),
            ("can_edit_interview_panel", "Can edit interview panel"),
            ("can_delete_interview_panel", "Can delete interview panel"),
            
            # Recruiter Permissions
            ("can_create_recruiter", "Can create recruiter"),
            ("can_view_recruiter", "Can view recruiter"),
            ("can_edit_recruiter", "Can edit recruiter"),
            ("can_delete_recruiter", "Can delete recruiter"),
        
            # Job Permissions
            ("can_create_job", "Can create job"),
            ("can_view_job", "Can view job"),
            ("can_edit_job", "Can edit job"),
            ("can_delete_job", "Can delete job"),
            ("can_assign_job", "Can assign job"),
            ("can_change_job_status", "Can change job status"),
            
            # Org Permissions
            ("can_create_organization", "Can create organization"),
        ]

class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client_type_name = models.CharField(max_length=100, choices=ATSUser.ROLE_CHOICES, null=True, blank=True)
    created_by = models.ForeignKey(ATSUser, on_delete=models.CASCADE, related_name='created_clients')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Client {self.id} - Type: {self.client_type_name}, Created by: {self.created_by}"

class JobSeeker(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(ATSUser, on_delete=models.CASCADE, related_name='job_seeker', unique=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    highest_education = models.CharField(max_length=100, null=True, blank=True)
    current_location = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    resume_file = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Job Seeker {self.id} - {self.first_name} {self.last_name}, Email: {self.email}"

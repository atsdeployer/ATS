from django.db import models
from django.conf import settings

class Organization(models.Model):
    org_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    info = models.JSONField()

    def __str__(self):
        return f"{self.name} (ID: {self.org_id})"

class User(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Manager', 'Manager'),
        ('HiringManager', 'Hiring Manager'),
        ('InterviewPanel', 'Interview Panel'),
        ('Recruiter', 'Recruiter'),
        ('JobSeeker', 'JobSeeker')
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    OrgID = models.ForeignKey(Organization, on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=50, null=True, blank=True)
    LastName = models.CharField(max_length=50, null=True, blank=True)
    Email = models.EmailField(unique=True)
    Phone = models.CharField(max_length=20, null=True, blank=True)
    PasswordText = models.CharField(max_length=255)
    Role = models.CharField(max_length=20, choices=ROLE_CHOICES, null=True, blank=True)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.FirstName} {self.LastName} - Role: {self.Role}"

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
    ClientID = models.AutoField(primary_key=True)
    ClientTypeName = models.CharField(max_length=100, choices=User.ROLE_CHOICES, null=True, blank=True)
    CreatedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Client {self.ClientID} - Type: {self.ClientTypeName}, Created by: {self.CreatedBy}"

class JobSeeker(models.Model):
    JobSeekerID = models.AutoField(primary_key=True)
    UserID = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    FirstName = models.CharField(max_length=50, null=True, blank=True)
    LastName = models.CharField(max_length=50, null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    Phone = models.CharField(max_length=20, null=True, blank=True)
    HighestEducation = models.CharField(max_length=100, null=True, blank=True)
    CurrentLocation = models.CharField(max_length=100, null=True, blank=True)
    State = models.CharField(max_length=50, null=True, blank=True)
    Country = models.CharField(max_length=50, null=True, blank=True)
    ResumeFile = models.CharField(max_length=255, null=True, blank=True)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Job Seeker {self.JobSeekerID} - {self.FirstName} {self.LastName}, Email: {self.Email}"

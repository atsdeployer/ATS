import uuid
from django.db import models
from AtsUser.models import *

class Skill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    skill_name = models.CharField(max_length=100, null=True, blank=True)
    skill_type = models.CharField(max_length=50, null=True, blank=True)
    is_custom_created = models.BooleanField(default=False)

    def __str__(self):
        return f"Skill {self.skill}: {self.skill_name} ({self.skill_type})"

class JobSeekerSkills(models.Model):
    job_seeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE, related_name='skills')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='job_seekers')

    def __str__(self):
        return f"{self.job_seeker} - Skill: {self.skill}"

class JobSeekerExperience(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job_seeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE, related_name='experiences')
    organization_name = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    experience_info = models.JSONField(default=dict)

    def __str__(self):
        return f"Experience {self.id} - {self.organization_name}, {self.start_date} to {self.end_date}"

class Certification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job_seeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE, unique=True, related_name='certification')
    certification_name = models.CharField(max_length=100, null=True, blank=True)
    certification_info = models.JSONField(default=dict)

    def __str__(self):
        return f"Certification {self.id}: {self.certification_name}"

class Job(models.Model):
    JOB_STATUS_CHOICES = [
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('in_progress', 'In Progress'),
        ('on_hold', 'On Hold'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='jobs')
    job_title = models.CharField(max_length=100, null=True, blank=True)
    requirement_number = models.CharField(max_length=50, null=True, blank=True)
    job_description = models.TextField(null=True, blank=True)
    job_status = models.CharField(max_length=50, choices=JOB_STATUS_CHOICES, null=True, blank=True)
    created_by = models.ForeignKey(ATSUser, on_delete=models.CASCADE, related_name='created_jobs')
    job_info = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Job {self.id}: {self.job_title} - Status: {self.job_status}"

class JobApplication(models.Model):
    APPLICATION_STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('in_review', 'In Review'),
        ('rejected', 'Rejected'),
        ('selected', 'Selected'),
        ('hired', 'Hired'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    job_seeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE, related_name='applications')
    application_status = models.CharField(max_length=50, choices=APPLICATION_STATUS_CHOICES, null=True, blank=True)
    application_info = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Application {self.id} - Job: {self.job}, Seeker: {self.job_seeker}, Status: {self.application_status}"

class InterviewPanelAssignment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='interview_panel_assignments')
    user = models.ForeignKey(ATSUser, on_delete=models.CASCADE, related_name='interview_assignments')
    assigned_by = models.ForeignKey(ATSUser, on_delete=models.CASCADE, related_name='assignments_made')
    assigned_at = models.DateTimeField(auto_now_add=True)
    interview_info = models.JSONField(default=dict)

    def __str__(self):
        return f"Assignment {self.id} - Job: {self.job}, Assigned by: {self.assigned_by}, At: {self.assigned_at}"

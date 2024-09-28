from django.db import models
from AtsUser.models import *

class Skill(models.Model):
    SkillID = models.AutoField(primary_key=True)
    SkillName = models.CharField(max_length=100, null=True, blank=True)
    SkillType = models.CharField(max_length=50, null=True, blank=True)
    IsCustomCreated = models.BooleanField(default=False)

    def __str__(self):
        return f"Skill {self.SkillID}: {self.SkillName} ({self.SkillType})"

class JobSeekerSkills(models.Model):
    JobSeekerID = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    SkillID = models.ForeignKey(Skill, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.JobSeekerID} - Skill: {self.SkillID}"

class JobSeekerExperience(models.Model):
    ExperienceID = models.AutoField(primary_key=True)
    JobSeekerID = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    OrganizationName = models.CharField(max_length=100, null=True, blank=True)
    StartDate = models.DateField(null=True, blank=True)
    EndDate = models.DateField(null=True, blank=True)
    ExperienceInfo = models.JSONField(default=dict)

    def __str__(self):
        return f"Experience {self.ExperienceID} - {self.OrganizationName}, {self.StartDate} to {self.EndDate}"

class Certification(models.Model):
    CertificationID = models.AutoField(primary_key=True)
    JobSeekerID = models.ForeignKey(JobSeeker, on_delete=models.CASCADE, unique=True)
    CertificationName = models.CharField(max_length=100, null=True, blank=True)
    CertificationInfo = models.JSONField(default=dict)

    def __str__(self):
        return f"Certification {self.CertificationID}: {self.CertificationName}"

class Job(models.Model):
    JOB_STATUS_CHOICES = [
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('in_progress', 'In Progress'),
        ('on_hold', 'On Hold'),
    ]

    JobID = models.AutoField(primary_key=True)
    ClientID = models.ForeignKey(Client, on_delete=models.CASCADE)
    JobTitle = models.CharField(max_length=100, null=True, blank=True)
    RequirementNumber = models.CharField(max_length=50, null=True, blank=True)
    JobDescription = models.TextField(null=True, blank=True)
    JobStatus = models.CharField(max_length=50, choices=JOB_STATUS_CHOICES, null=True, blank=True)
    CreatedBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs_created')
    JobInfo = models.JSONField(default=dict)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Job {self.JobID}: {self.JobTitle} - Status: {self.JobStatus}"

class JobApplication(models.Model):
    APPLICATION_STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('in_review', 'In Review'),
        ('rejected', 'Rejected'),
        ('selected', 'Selected'),
        ('hired', 'Hired'),
    ]

    ApplicationID = models.AutoField(primary_key=True)
    JobID = models.ForeignKey(Job, on_delete=models.CASCADE)
    JobSeekerID = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    ApplicationStatus = models.CharField(max_length=50, choices=APPLICATION_STATUS_CHOICES, null=True, blank=True)
    ApplicationInfo = models.JSONField(default=dict)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Application {self.ApplicationID} - Job: {self.JobID}, Seeker: {self.JobSeekerID}, Status: {self.ApplicationStatus}"

class InterviewPanelAssignment(models.Model):
    AssignmentID = models.AutoField(primary_key=True)
    JobID = models.ForeignKey(Job, on_delete=models.CASCADE)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    AssignedBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assignments_made')
    AssignedAt = models.DateTimeField(auto_now_add=True)
    InterviewInfo = models.JSONField(default=dict)

    def __str__(self):
        return f"Assignment {self.AssignmentID} - Job: {self.JobID}, Assigned by: {self.AssignedBy}, At: {self.AssignedAt}"

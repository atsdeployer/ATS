from django.contrib import admin
from .models import *

admin.site.register(Job)
admin.site.register(Skill)
admin.site.register(Certification)
admin.site.register(JobApplication)
admin.site.register(JobSeekerSkills)
admin.site.register(JobSeekerExperience)
admin.site.register(InterviewPanelAssignment)
# job/serializers.py

from rest_framework import serializers
from .models import *

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class JobSeekerSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSeekerSkills
        fields = '__all__'

class JobSeekerExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSeekerExperience
        fields = '__all__'

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
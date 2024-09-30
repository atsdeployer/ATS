from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serializers import *

class SkillView(APIView):
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SkillDetailView(APIView):
    def get(self, request, pk):
        try:
            skill = Skill.objects.get(pk=pk)
            serializer = SkillSerializer(skill)
            return Response(serializer.data)
        except Skill.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            skill = Skill.objects.get(pk=pk)
            serializer = SkillSerializer(skill, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Skill.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            skill = Skill.objects.get(pk=pk)
            skill.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Skill.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
class JobView(APIView):
    def get(self, request):
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JobDetailView(APIView):
    def get(self, request, pk):
        try:
            job = Job.objects.get(pk=pk)
            serializer = JobSerializer(job)
            return Response(serializer.data)
        except Job.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            job = Job.objects.get(pk=pk)
            serializer = JobSerializer(job, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Job.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            job = Job.objects.get(pk=pk)
            job.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Job.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class JobSeekerSkillsView(APIView):
    def get(self, request):
        job_seeker_skills = JobSeekerSkills.objects.all()
        serializer = JobSeekerSkillsSerializer(job_seeker_skills, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JobSeekerSkillsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JobSeekerSkillsDetailView(APIView):
    def get(self, request, pk):
        try:
            job_seeker_skills = JobSeekerSkills.objects.get(pk=pk)
            serializer = JobSeekerSkillsSerializer(job_seeker_skills)
            return Response(serializer.data)
        except JobSeekerSkills.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            job_seeker_skills = JobSeekerSkills.objects.get(pk=pk)
            serializer = JobSeekerSkillsSerializer(job_seeker_skills, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JobSeekerSkills.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            job_seeker_skills = JobSeekerSkills.objects.get(pk=pk)
            job_seeker_skills.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except JobSeekerSkills.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class JobSeekerExperienceView(APIView):
    def get(self, request):
        job_seeker_experiences = JobSeekerExperience.objects.all()
        serializer = JobSeekerExperienceSerializer(job_seeker_experiences, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JobSeekerExperienceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JobSeekerExperienceDetailView(APIView):
    def get(self, request, pk):
        try:
            job_seeker_experience = JobSeekerExperience.objects.get(pk=pk)
            serializer = JobSeekerExperienceSerializer(job_seeker_experience)
            return Response(serializer.data)
        except JobSeekerExperience.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            job_seeker_experience = JobSeekerExperience.objects.get(pk=pk)
            serializer = JobSeekerExperienceSerializer(job_seeker_experience, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JobSeekerExperience.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            job_seeker_experience = JobSeekerExperience.objects.get(pk=pk)
            job_seeker_experience.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except JobSeekerExperience.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class JobSeekerEducationView(APIView):
    def get(self, request):
        job_seeker_educations = JobSeekerEducation.objects.all()
        serializer = JobSeekerEducationSerializer(job_seeker_educations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JobSeekerEducationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JobSeekerEducationDetailView(APIView):
    def get(self, request, pk):
        try:
            job_seeker_education = JobSeekerEducation.objects.get(pk=pk)
            serializer = JobSeekerEducationSerializer(job_seeker_education)
            return Response(serializer.data)
        except JobSeekerEducation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            job_seeker_education = JobSeekerEducation.objects.get(pk=pk)
            serializer = JobSeekerEducationSerializer(job_seeker_education, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JobSeekerEducation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            job_seeker_education = JobSeekerEducation.objects.get(pk=pk)
            job_seeker_education.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except JobSeekerEducation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class CertificationView(APIView):
    def get(self, request):
        certifications = Certification.objects.all()
        serializer = CertificationSerializer(certifications, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CertificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CertificationDetailView(APIView):
    def get(self, request, pk):
        try:
            certification = Certification.objects.get(pk=pk)
            serializer = CertificationSerializer(certification)
            return Response(serializer.data)
        except Certification.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            certification = Certification.objects.get(pk=pk)
            serializer = CertificationSerializer(certification, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Certification.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            certification = Certification.objects.get(pk=pk)
            certification.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Certification.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class JobApplicationView(APIView):
    def get(self, request):
        job_applications = JobApplication.objects.all()
        serializer = JobApplicationSerializer(job_applications, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JobApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JobApplicationDetailView(APIView):
    def get(self, request, pk):
        try:
            job_application = JobApplication.objects.get(pk=pk)
            serializer = JobApplicationSerializer(job_application)
            return Response(serializer.data)
        except JobApplication.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            job_application = JobApplication.objects.get(pk=pk)
            serializer = JobApplicationSerializer(job_application, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JobApplication.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            job_application = JobApplication.objects.get(pk=pk)
            job_application.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except JobApplication.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class InterviewPanelAssignmentView(APIView):
    def get(self, request):
        interview_panel_assignments = InterviewPanelAssignment.objects.all()
        serializer = InterviewPanelAssignmentSerializer(interview_panel_assignments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InterviewPanelAssignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InterviewPanelAssignmentDetailView(APIView):
    def get(self, request, pk):
        try:
            interview_panel_assignment = InterviewPanelAssignment.objects.get(pk=pk)
            serializer = InterviewPanelAssignmentSerializer(interview_panel_assignment)
            return Response(serializer.data)
        except InterviewPanelAssignment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            interview_panel_assignment = InterviewPanelAssignment.objects.get(pk=pk)
            serializer = InterviewPanelAssignmentSerializer(interview_panel_assignment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except InterviewPanelAssignment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            interview_panel_assignment = InterviewPanelAssignment.objects.get(pk=pk)
            interview_panel_assignment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except InterviewPanelAssignment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
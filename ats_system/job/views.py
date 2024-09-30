from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .models import *
from .serializers import *

class SkillView(APIView):
    @swagger_auto_schema(
        operation_summary="List all skills",
        responses={200: SkillSerializer(many=True)}
    )
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create a new skill",
        request_body=SkillSerializer,
        responses={
            201: SkillSerializer,
            400: "Validation error"
        }
    )
    def post(self, request):
        serializer = SkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SkillDetailView(APIView):
    @swagger_auto_schema(
        operation_summary="Retrieve a skill by ID",
        responses={
            200: SkillSerializer,
            404: "Skill not found"
        }
    )
    def get(self, request, pk):
        try:
            skill = Skill.objects.get(pk=pk)
            serializer = SkillSerializer(skill)
            return Response(serializer.data)
        except Skill.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_summary="Update a skill",
        request_body=SkillSerializer,
        responses={
            200: SkillSerializer,
            400: "Validation error",
            404: "Skill not found"
        }
    )
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

    @swagger_auto_schema(
        operation_summary="Delete a skill",
        responses={204: "No content", 404: "Skill not found"}
    )
    def delete(self, request, pk):
        try:
            skill = Skill.objects.get(pk=pk)
            skill.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Skill.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class JobView(APIView):
    @swagger_auto_schema(
        operation_summary="List all jobs",
        responses={200: JobSerializer(many=True)}
    )
    def get(self, request):
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create a new job",
        request_body=JobSerializer,
        responses={
            201: JobSerializer,
            400: "Validation error"
        }
    )
    def post(self, request):
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JobDetailView(APIView):
    @swagger_auto_schema(
        operation_summary="Retrieve a job by ID",
        responses={
            200: JobSerializer,
            404: "Job not found"
        }
    )
    def get(self, request, pk):
        try:
            job = Job.objects.get(pk=pk)
            serializer = JobSerializer(job)
            return Response(serializer.data)
        except Job.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_summary="Update a job",
        request_body=JobSerializer,
        responses={
            200: JobSerializer,
            400: "Validation error",
            404: "Job not found"
        }
    )
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

    @swagger_auto_schema(
        operation_summary="Delete a job",
        responses={204: "No content", 404: "Job not found"}
    )
    def delete(self, request, pk):
        try:
            job = Job.objects.get(pk=pk)
            job.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Job.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class JobSeekerSkillsView(APIView):
    @swagger_auto_schema(
        operation_summary="List all job seeker skills",
        responses={200: JobSeekerSkillsSerializer(many=True)}
    )
    def get(self, request):
        job_seeker_skills = JobSeekerSkills.objects.all()
        serializer = JobSeekerSkillsSerializer(job_seeker_skills, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create a new job seeker skill",
        request_body=JobSeekerSkillsSerializer,
        responses={
            201: JobSeekerSkillsSerializer,
            400: "Validation error"
        }
    )
    def post(self, request):
        serializer = JobSeekerSkillsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JobSeekerSkillsDetailView(APIView):
    @swagger_auto_schema(
        operation_summary="Retrieve a job seeker skill by ID",
        responses={
            200: JobSeekerSkillsSerializer,
            404: "Job seeker skill not found"
        }
    )
    def get(self, request, pk):
        try:
            job_seeker_skill = JobSeekerSkills.objects.get(pk=pk)
            serializer = JobSeekerSkillsSerializer(job_seeker_skill)
            return Response(serializer.data)
        except JobSeekerSkills.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_summary="Update a job seeker skill",
        request_body=JobSeekerSkillsSerializer,
        responses={
            200: JobSeekerSkillsSerializer,
            400: "Validation error",
            404: "Job seeker skill not found"
        }
    )
    def put(self, request, pk):
        try:
            job_seeker_skill = JobSeekerSkills.objects.get(pk=pk)
            serializer = JobSeekerSkillsSerializer(job_seeker_skill, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JobSeekerSkills.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_summary="Delete a job seeker skill",
        responses={204: "No content", 404: "Job seeker skill not found"}
    )
    def delete(self, request, pk):
        try:
            job_seeker_skill = JobSeekerSkills.objects.get(pk=pk)
            job_seeker_skill.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except JobSeekerSkills.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class JobSeekerExperienceView(APIView):
    @swagger_auto_schema(
        operation_summary="List all job seeker experiences",
        responses={200: JobSeekerExperienceSerializer(many=True)}
    )
    def get(self, request):
        job_seeker_experiences = JobSeekerExperience.objects.all()
        serializer = JobSeekerExperienceSerializer(job_seeker_experiences, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create a new job seeker experience",
        request_body=JobSeekerExperienceSerializer,
        responses={
            201: JobSeekerExperienceSerializer,
            400: "Validation error"
        }
    )
    def post(self, request):
        serializer = JobSeekerExperienceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JobSeekerExperienceDetailView(APIView):
    @swagger_auto_schema(
        operation_summary="Retrieve a job seeker experience by ID",
        responses={
            200: JobSeekerExperienceSerializer,
            404: "Job seeker experience not found"
        }
    )
    def get(self, request, pk):
        try:
            job_seeker_experience = JobSeekerExperience.objects.get(pk=pk)
            serializer = JobSeekerExperienceSerializer(job_seeker_experience)
            return Response(serializer.data)
        except JobSeekerExperience.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_summary="Update a job seeker experience",
        request_body=JobSeekerExperienceSerializer,
        responses={
            200: JobSeekerExperienceSerializer,
            400: "Validation error",
            404: "Job seeker experience not found"
        }
    )
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

    @swagger_auto_schema(
        operation_summary="Delete a job seeker experience",
        responses={204: "No content", 404: "Job seeker experience not found"}
    )
    def delete(self, request, pk):
        try:
            job_seeker_experience = JobSeekerExperience.objects.get(pk=pk)
            job_seeker_experience.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except JobSeekerExperience.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class JobSeekerEducationView(APIView):
    @swagger_auto_schema(
        operation_summary="List all job seeker educations",
        responses={200: JobSeekerEducationSerializer(many=True)}
    )
    def get(self, request):
        job_seeker_educations = JobSeekerEducation.objects.all()
        serializer = JobSeekerEducationSerializer(job_seeker_educations, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create a new job seeker education",
        request_body=JobSeekerEducationSerializer,
        responses={
            201: JobSeekerEducationSerializer,
            400: "Validation error"
        }
    )
    def post(self, request):
        serializer = JobSeekerEducationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JobSeekerEducationDetailView(APIView):
    @swagger_auto_schema(
        operation_summary="Retrieve a job seeker education by ID",
        responses={
            200: JobSeekerEducationSerializer,
            404: "Job seeker education not found"
        }
    )
    def get(self, request, pk):
        try:
            job_seeker_education = JobSeekerEducation.objects.get(pk=pk)
            serializer = JobSeekerEducationSerializer(job_seeker_education)
            return Response(serializer.data)
        except JobSeekerEducation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_summary="Update a job seeker education",
        request_body=JobSeekerEducationSerializer,
        responses={
            200: JobSeekerEducationSerializer,
            400: "Validation error",
            404: "Job seeker education not found"
        }
    )
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

    @swagger_auto_schema(
        operation_summary="Delete a job seeker education",
        responses={204: "No content", 404: "Job seeker education not found"}
    )
    def delete(self, request, pk):
        try:
            job_seeker_education = JobSeekerEducation.objects.get(pk=pk)
            job_seeker_education.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except JobSeekerEducation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class CertificationView(APIView):
    @swagger_auto_schema(
        operation_summary="List all certifications",
        responses={200: CertificationSerializer(many=True)}
    )
    def get(self, request):
        certifications = Certification.objects.all()
        serializer = CertificationSerializer(certifications, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create a new certification",
        request_body=CertificationSerializer,
        responses={
            201: CertificationSerializer,
            400: "Validation error"
        }
    )
    def post(self, request):
        serializer = CertificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CertificationDetailView(APIView):
    @swagger_auto_schema(
        operation_summary="Retrieve a certification by ID",
        responses={
            200: CertificationSerializer,
            404: "Certification not found"
        }
    )
    def get(self, request, pk):
        try:
            certification = Certification.objects.get(pk=pk)
            serializer = CertificationSerializer(certification)
            return Response(serializer.data)
        except Certification.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_summary="Update a certification",
        request_body=CertificationSerializer,
        responses={
            200: CertificationSerializer,
            400: "Validation error",
            404: "Certification not found"
        }
    )
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

    @swagger_auto_schema(
        operation_summary="Delete a certification",
        responses={204: "No content", 404: "Certification not found"}
    )
    def delete(self, request, pk):
        try:
            certification = Certification.objects.get(pk=pk)
            certification.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Certification.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class JobApplicationView(APIView):
    @swagger_auto_schema(
        operation_summary="List all job applications",
        responses={200: JobApplicationSerializer(many=True)}
    )
    def get(self, request):
        job_applications = JobApplication.objects.all()
        serializer = JobApplicationSerializer(job_applications, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create a new job application",
        request_body=JobApplicationSerializer,
        responses={
            201: JobApplicationSerializer,
            400: "Validation error"
        }
    )
    def post(self, request):
        serializer = JobApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JobApplicationDetailView(APIView):
    @swagger_auto_schema(
        operation_summary="Retrieve a job application by ID",
        responses={
            200: JobApplicationSerializer,
            404: "Job application not found"
        }
    )
    def get(self, request, pk):
        try:
            job_application = JobApplication.objects.get(pk=pk)
            serializer = JobApplicationSerializer(job_application)
            return Response(serializer.data)
        except JobApplication.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_summary="Update a job application",
        request_body=JobApplicationSerializer,
        responses={
            200: JobApplicationSerializer,
            400: "Validation error",
            404: "Job application not found"
        }
    )
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

    @swagger_auto_schema(
        operation_summary="Delete a job application",
        responses={204: "No content", 404: "Job application not found"}
    )
    def delete(self, request, pk):
        try:
            job_application = JobApplication.objects.get(pk=pk)
            job_application.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except JobApplication.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class InterviewPanelAssignmentView(APIView):
    @swagger_auto_schema(
        operation_summary="List all interview panel assignments",
        responses={200: InterviewPanelAssignmentSerializer(many=True)}
    )
    def get(self, request):
        interview_panel_assignments = InterviewPanelAssignment.objects.all()
        serializer = InterviewPanelAssignmentSerializer(interview_panel_assignments, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create a new interview panel assignment",
        request_body=InterviewPanelAssignmentSerializer,
        responses={
            201: InterviewPanelAssignmentSerializer,
            400: "Validation error"
        }
    )
    def post(self, request):
        serializer = InterviewPanelAssignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InterviewPanelAssignmentDetailView(APIView):
    @swagger_auto_schema(
        operation_summary="Retrieve an interview panel assignment by ID",
        responses={
            200: InterviewPanelAssignmentSerializer,
            404: "Interview panel assignment not found"
        }
    )
    def get(self, request, pk):
        try:
            assignment = InterviewPanelAssignment.objects.get(pk=pk)
            serializer = InterviewPanelAssignmentSerializer(assignment)
            return Response(serializer.data)
        except InterviewPanelAssignment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_summary="Update an interview panel assignment",
        request_body=InterviewPanelAssignmentSerializer,
        responses={
            200: InterviewPanelAssignmentSerializer,
            400: "Validation error",
            404: "Interview panel assignment not found"
        }
    )
    def put(self, request, pk):
        try:
            assignment = InterviewPanelAssignment.objects.get(pk=pk)
            serializer = InterviewPanelAssignmentSerializer(assignment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except InterviewPanelAssignment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_summary="Delete an interview panel assignment",
        responses={204: "No content", 404: "Interview panel assignment not found"}
    )
    def delete(self, request, pk):
        try:
            assignment = InterviewPanelAssignment.objects.get(pk=pk)
            assignment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except InterviewPanelAssignment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

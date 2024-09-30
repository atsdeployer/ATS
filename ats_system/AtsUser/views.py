from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

class OrganizationView(APIView):
    @swagger_auto_schema(
        operation_summary="List all organizations",
        responses={200: "List of organizations"}
    )
    def get(self, request):
        organizations = Organization.objects.all()
        serializer = OrganizationSerializer(organizations, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create a new organization",
        request_body=OrganizationSerializer,
        responses={
            201: OrganizationSerializer,
            400: "Validation error"
        }
    )
    def post(self, request):
        serializer = OrganizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrganizationDetailView(APIView):
    @swagger_auto_schema(
        operation_summary="Retrieve an organization by ID",
        responses={
            200: OrganizationSerializer,
            404: "Organization not found"
        }
    )
    def get(self, request, pk):
        try:
            organization = Organization.objects.get(pk=pk)
            serializer = OrganizationSerializer(organization)
            return Response(serializer.data)
        except Organization.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_summary="Update an organization",
        request_body=OrganizationSerializer,
        responses={
            200: OrganizationSerializer,
            400: "Validation error",
            404: "Organization not found"
        }
    )
    def put(self, request, pk):
        try:
            organization = Organization.objects.get(pk=pk)
            serializer = OrganizationSerializer(organization, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Organization.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_summary="Delete an organization",
        responses={204: "No content", 404: "Organization not found"}
    )
    def delete(self, request, pk):
        try:
            organization = Organization.objects.get(pk=pk)
            organization.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Organization.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class ATSUserView(APIView):
    @swagger_auto_schema(
        operation_summary="List all ATS users",
        responses={200: "List of ATS users"}
    )
    def get(self, request):
        ats_users = ATSUser.objects.all()
        serializer = ATSUserSerializer(ats_users, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create a new ATS user",
        request_body=ATSUserSerializer,
        responses={
            201: ATSUserSerializer,
            400: "Validation error"
        }
    )
    def post(self, request):
        serializer = ATSUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ATSUserDetailView(APIView):
    @swagger_auto_schema(
        operation_summary="Retrieve an ATS user by ID",
        responses={
            200: ATSUserSerializer,
            404: "ATS user not found"
        }
    )
    def get(self, request, pk):
        try:
            ats_user = ATSUser.objects.get(pk=pk)
            serializer = ATSUserSerializer(ats_user)
            return Response(serializer.data)
        except ATSUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_summary="Update an ATS user",
        request_body=ATSUserSerializer,
        responses={
            200: ATSUserSerializer,
            400: "Validation error",
            404: "ATS user not found"
        }
    )
    def put(self, request, pk):
        try:
            ats_user = ATSUser.objects.get(pk=pk)
            serializer = ATSUserSerializer(ats_user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ATSUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_summary="Delete an ATS user",
        responses={204: "No content", 404: "ATS user not found"}
    )
    def delete(self, request, pk):
        try:
            ats_user = ATSUser.objects.get(pk=pk)
            ats_user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ATSUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class JobSeekerView(APIView):
    @swagger_auto_schema(
        operation_summary="List all job seekers",
        responses={200: "List of job seekers"}
    )
    def get(self, request):
        job_seekers = JobSeeker.objects.all()
        serializer = JobSeekerSerializer(job_seekers, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create a new job seeker",
        request_body=JobSeekerSerializer,
        responses={
            201: JobSeekerSerializer,
            400: "Validation error"
        }
    )
    def post(self, request):
        serializer = JobSeekerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JobSeekerDetailView(APIView):
    @swagger_auto_schema(
        operation_summary="Retrieve a job seeker by ID",
        responses={
            200: JobSeekerSerializer,
            404: "Job seeker not found"
        }
    )
    def get(self, request, pk):
        try:
            job_seeker = JobSeeker.objects.get(pk=pk)
            serializer = JobSeekerSerializer(job_seeker)
            return Response(serializer.data)
        except JobSeeker.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_summary="Update a job seeker",
        request_body=JobSeekerSerializer,
        responses={
            200: JobSeekerSerializer,
            400: "Validation error",
            404: "Job seeker not found"
        }
    )
    def put(self, request, pk):
        try:
            job_seeker = JobSeeker.objects.get(pk=pk)
            serializer = JobSeekerSerializer(job_seeker, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JobSeeker.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_summary="Delete a job seeker",
        responses={204: "No content", 404: "Job seeker not found"}
    )
    def delete(self, request, pk):
        try:
            job_seeker = JobSeeker.objects.get(pk=pk)
            job_seeker.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except JobSeeker.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

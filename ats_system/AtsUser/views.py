from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serializers import *

class OrganizationView(APIView):
    def get(self, request):
        organizations = Organization.objects.all()
        serializer = OrganizationSerializer(organizations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrganizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrganizationDetailView(APIView):
    def get(self, request, pk):
        try:
            organization = Organization.objects.get(pk=pk)
            serializer = OrganizationSerializer(organization)
            return Response(serializer.data)
        except Organization.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

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

    def delete(self, request, pk):
        try:
            organization = Organization.objects.get(pk=pk)
            organization.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Organization.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class ATSUserView(APIView):
    def get(self, request):
        ats_users = ATSUser.objects.all()
        serializer = ATSUserSerializer(ats_users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ATSUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ATSUserDetailView(APIView):
    def get(self, request, pk):
        try:
            ats_user = ATSUser.objects.get(pk=pk)
            serializer = ATSUserSerializer(ats_user)
            return Response(serializer.data)
        except ATSUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

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

    def delete(self, request, pk):
        try:
            ats_user = ATSUser.objects.get(pk=pk)
            ats_user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ATSUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class JobSeekerView(APIView):
    def get(self, request):
        job_seekers = JobSeeker.objects.all()
        serializer = JobSeekerSerializer(job_seekers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JobSeekerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JobSeekerDetailView(APIView):
    def get(self, request, pk):
        try:
            job_seeker = JobSeeker.objects.get(pk=pk)
            serializer = JobSeekerSerializer(job_seeker)
            return Response(serializer.data)
        except JobSeeker.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

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

    def delete(self, request, pk):
        try:
            job_seeker = JobSeeker.objects.get(pk=pk)
            job_seeker.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except JobSeeker.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

from django.contrib.auth.models import User
from django.test import TestCase
from AtsUser.models import *

class OrganizationTest(TestCase):
    def setUp(self):
        self.organization = Organization.objects.create(name="Test Org", info={})

    def test_organization_creation(self):
        self.assertTrue(isinstance(self.organization, Organization))
        self.assertEqual(str(self.organization), f"{self.organization.name} (ID: {self.organization.id})")

class ATSUserTest(TestCase):
    def setUp(self):
        self.organization = Organization.objects.create(name="Test Org", info={})
        self.user = User.objects.create(
            username='testuser',
            password='testpassword'
        )
        self.ats_user = ATSUser.objects.create(
            user = self.user,
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            organization=self.organization,
            role="JobSeeker",
            password_text="dummy_password"
        )
    def get_ats_user(self):
        self.setUp()
        return self.ats_user

    def test_atsuser_creation(self):
        self.assertTrue(isinstance(self.ats_user, ATSUser))
        self.assertEqual(str(self.ats_user), f"{self.ats_user.first_name} {self.ats_user.last_name} - Role: {self.ats_user.role}")

class JobSeekerTest(TestCase):
    def setUp(self):
        ats_user_test = ATSUserTest()
        self.ats_user = ats_user_test.get_ats_user()

    def test_job_seeker_creation(self):
        job_seeker = JobSeeker.objects.create(
            user=self.ats_user,
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            phone="1234567890"
        )
        self.assertTrue(isinstance(job_seeker, JobSeeker))
        self.assertEqual(str(job_seeker), f"Job Seeker {job_seeker.id} - {job_seeker.first_name} {job_seeker.last_name}, Email: {job_seeker.email}")
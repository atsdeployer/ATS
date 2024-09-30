from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from AtsUser.models import ATSUser, Organization
from .models import Skill, JobSeeker, JobSeekerSkills, JobSeekerExperience, Certification, Job, JobApplication, InterviewPanelAssignment
import uuid

class SkillModelTest(TestCase):

    def setUp(self):
        self.skill = Skill.objects.create(
            skill_name="Django",
            skill_type="Technical",
            is_custom_created=True
        )

    def test_skill_creation(self):
        skill = Skill(skill_name="Django", skill_type="Technical", is_custom_created=True)
        skill.save()  # Save the object to generate the UUID
        self.assertTrue(isinstance(skill, Skill))
        self.assertEqual(str(skill), f"Skill {skill.id}: Django (Technical)")


    def test_blank_skill_name(self):
        skill = Skill.objects.create(skill_name="", skill_type="Technical")
        self.assertEqual(skill.skill_name, "")

    def test_skill_type_max_length(self):
        skill = Skill.objects.get(id=self.skill.id)
        max_length = skill._meta.get_field('skill_type').max_length
        self.assertEqual(max_length, 50)


class JobSeekerSkillsTest(TestCase):

    def setUp(self):
        self.organization = Organization.objects.create(name="Test Org", info={})
        self.user = User.objects.create(
            username='testuser',
            password='testpassword'
        )
        self.ats_user = ATSUser.objects.create(
            user = self.user,
            first_name="Alice",
            last_name="Johnson",
            email="alice.johnson@example.com",
            organization=self.organization,
            role="JobSeeker",
            password_text="dummy_password"
        )
        self.job_seeker = JobSeeker.objects.create(
            user=self.ats_user,
            first_name="Alice",
            last_name="Johnson",
            email="alice.johnson@example.com",
            phone="1234567890"
        )
        self.skill = Skill.objects.create(
            skill_name="Python",
            skill_type="Technical"
        )
        self.job_seeker_skill = JobSeekerSkills.objects.create(
            job_seeker=self.job_seeker,
            skill=self.skill
        )

    def test_job_seeker_skill_creation(self):
        job_seeker_skill = self.job_seeker_skill
        self.assertTrue(isinstance(job_seeker_skill, JobSeekerSkills))
        self.assertEqual(str(job_seeker_skill), f"{self.job_seeker} - Skill: {self.skill}")

    def test_job_seeker_skill_relationship(self):
        self.assertEqual(self.job_seeker_skill.skill.skill_name, "Python")
        self.assertEqual(self.job_seeker_skill.job_seeker.first_name, "Alice")


class JobSeekerExperienceModelTest(TestCase):

    def setUp(self):
        self.organization = Organization.objects.create(name="Test Org", info={})
        self.user = User.objects.create(
            username='testuser',
            password='testpassword'
        )
        self.ats_user = ATSUser.objects.create(
            user = self.user,
            first_name="Bob",
            last_name="Smith",
            email="bob.smith@example.com",
            organization=self.organization,
            role="JobSeeker",
            password_text="dummy_password"
        )
        self.job_seeker = JobSeeker.objects.create(
            user=self.ats_user,
            first_name="Bob",
            last_name="Smith",
            email="bob.smith@example.com",
            phone="0987654321"
        )
        self.experience = JobSeekerExperience.objects.create(
            job_seeker=self.job_seeker,
            organization_name="Tech Corp",
            start_date=timezone.datetime(2022, 1, 1).date(),
            end_date=timezone.datetime(2023, 1, 1).date(),
            experience_info={"position": "Software Engineer"}
        )

    def test_experience_creation(self):
        experience = self.experience
        self.assertTrue(isinstance(experience, JobSeekerExperience))
        self.assertEqual(str(experience), f"Experience {experience.id} - Tech Corp, 2022-01-01 to 2023-01-01")

    def test_experience_dates(self):
        experience = self.experience
        self.assertEqual(experience.start_date, timezone.datetime(2022, 1, 1).date())
        self.assertEqual(experience.end_date, timezone.datetime(2023, 1, 1).date())

    def test_experience_info(self):
        experience = self.experience
        self.assertEqual(experience.experience_info['position'], "Software Engineer")


class CertificationModelTest(TestCase):

    def setUp(self):
        self.organization = Organization.objects.create(name="Test Org", info={})
        self.user = User.objects.create(
            username='testuser',
            password='testpassword'
        )
        self.ats_user = ATSUser.objects.create(
            user = self.user,
            first_name="Carol",
            last_name="Brown",
            email="carol.brown@example.com",
            organization=self.organization,
            role="JobSeeker",
            password_text="dummy_password"
        )
        self.job_seeker = JobSeeker.objects.create(
            user=self.ats_user,
            first_name="Carol",
            last_name="Brown",
            email="carol.brown@example.com",
            phone="1112223333"
        )
        self.certification = Certification.objects.create(
            job_seeker=self.job_seeker,
            certification_name="AWS Certified Solutions Architect",
            certification_info={"provider": "AWS"}
        )

    def test_certification_creation(self):
        certification = self.certification
        self.assertTrue(isinstance(certification, Certification))
        self.assertEqual(str(certification), f"Certification {certification.id}: AWS Certified Solutions Architect")

    def test_certification_info(self):
        certification = self.certification
        self.assertEqual(certification.certification_info['provider'], "AWS")


class JobApplicationStatusTest(TestCase):

    def setUp(self):
        self.organization = Organization.objects.create(name="Test Org", info={})
        self.user = User.objects.create(
            username='testuser',
            password='testpassword'
        )
        self.ats_user = ATSUser.objects.create(
            user=self.user,
            first_name="Dan",
            last_name="White",
            email="dan.white@example.com",
            organization=self.organization,
            role="Manager",
            password_text="dummy_password"
        )
        self.job = Job.objects.create(
            user=self.ats_user,
            created_by=self.ats_user,
            job_title="Data Analyst",
            job_status="open",
            job_info={"description": "Analyze data"}
        )
        self.job_seeker = JobSeeker.objects.create(
            user=self.ats_user,
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            phone="1234567890"
        )
        self.job_application = JobApplication.objects.create(
            job=self.job,
            job_seeker=self.job_seeker,
            application_status="applied",
            application_info={"info": "Test application"}
        )

    def test_application_status_choices(self):
        job_application = self.job_application
        choices = [choice[0] for choice in JobApplication.APPLICATION_STATUS_CHOICES]
        self.assertIn(job_application.application_status, choices)

    def test_application_update_status(self):
        job_application = self.job_application
        job_application.application_status = "in_review"
        job_application.save()
        self.assertEqual(job_application.application_status, "in_review")


class InterviewPanelAssignmentTest(TestCase):

    def setUp(self):
        self.organization = Organization.objects.create(name="Test Org", info={})
        self.user = User.objects.create(
            username='testuser',
            password='testpassword'
        )
        self.manager = ATSUser.objects.create(
            user=self.user,
            first_name="Eve",
            last_name="Black",
            email="eve.black@example.com",
            organization=self.organization,
            role="Manager",
            password_text="dummy_password"
        )
        self.job = Job.objects.create(
            user=self.manager,
            created_by=self.manager,
            job_title="Frontend Developer",
            job_status="open",
            job_info={"description": "Frontend work"}
        )
        self.user1 = User.objects.create(
            username='testuser1',
            password='testpassword'
        )
        self.panel_user = ATSUser.objects.create(
            user=self.user1,
            first_name="Sam",
            last_name="Green",
            email="sam.green@example.com",
            organization=self.organization,
            role="InterviewPanel",
            password_text="dummy_password"
        )
        self.assignment = InterviewPanelAssignment.objects.create(
            job=self.job,
            user=self.panel_user,
            assigned_by=self.manager,
            interview_info={"role": "Lead Interviewer"}
        )

    def test_interview_panel_assignment(self):
        assignment = self.assignment
        self.assertTrue(isinstance(assignment, InterviewPanelAssignment))
        self.assertEqual(str(assignment), f"Assignment {assignment.id} - Job: {self.job}, Assigned by: {self.manager}, At: {assignment.assigned_at}")

    def test_interview_panel_relationship(self):
        self.assertEqual(self.assignment.user.first_name, "Sam")
        self.assertEqual(self.assignment.assigned_by.first_name, "Eve")

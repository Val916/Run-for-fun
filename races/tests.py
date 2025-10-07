from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Race


class RaceVisibilityTestCase(TestCase):
    """
    Test case for Race model visibility logic.
    Tests the is_visible_to_user method with different user types.
    """
    
    def setUp(self):
        """
        Set up test data that will be used in multiple test methods.
        This method runs before each individual test method.
        """
        # Create test users
        self.regular_user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        
        self.race_creator = User.objects.create_user(
            username='creator',
            email='creator@example.com',
            password='creatorpass123'
        )
        
        self.admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpass123'
        )
        
        # Create test races
        self.public_race = Race.objects.create(
            name='Public Race',
            description='A public race everyone can see',
            city='Test City',
            race_date=timezone.now().date(),
            distance='5K',
            difficulty='EASY_PEASY',
            status=1,  # Published status
            approved=True,  # Approved by admin
            created_by=self.race_creator
        )
        
        self.private_race = Race.objects.create(
            name='Private Race',
            description='A private race only creator and admin can see',
            city='Test City',
            race_date=timezone.now().date(),
            distance='HALF',
            difficulty='ADULTS_ONLY',
            status=0,  # Draft status (not published)
            approved=False,  # Not approved
            created_by=self.race_creator
        )

    def test_public_race_visible_to_anonymous_user(self):
        """
        Test that public races are visible to anonymous (not logged in) users.
        """
        # Create an anonymous user (not authenticated)
        from django.contrib.auth.models import AnonymousUser
        anonymous_user = AnonymousUser()
        
        # Test: Public race should be visible to anonymous user
        result = self.public_race.is_visible_to_user(anonymous_user)
        self.assertTrue(result, "Public race should be visible to anonymous user")
        
        # Test: Private race should NOT be visible to anonymous user
        result = self.private_race.is_visible_to_user(anonymous_user)
        self.assertFalse(result, "Private race should not be visible to anonymous user")

    def test_public_race_visible_to_regular_user(self):
        """
        Test that public races are visible to regular authenticated users.
        """
        # Test: Public race should be visible to regular user
        result = self.public_race.is_visible_to_user(self.regular_user)
        self.assertTrue(result, "Public race should be visible to regular user")

    def test_private_race_visible_to_creator(self):
        """
        Test that private races are visible to their creators.
        """
        # Test: Private race should be visible to its creator
        result = self.private_race.is_visible_to_user(self.race_creator)
        self.assertTrue(result, "Private race should be visible to its creator")
        
        # Test: Private race should NOT be visible to other regular users
        result = self.private_race.is_visible_to_user(self.regular_user)
        self.assertFalse(result, "Private race should not be visible to other users")

    def test_all_races_visible_to_admin(self):
        """
        Test that admin users can see all races (both public and private).
        """
        # Test: Admin should see public race
        result = self.public_race.is_visible_to_user(self.admin_user)
        self.assertTrue(result, "Admin should see public race")
        
        # Test: Admin should see private race
        result = self.private_race.is_visible_to_user(self.admin_user)
        self.assertTrue(result, "Admin should see private race")

    def test_race_string_representation(self):
        """
        Test the __str__ method of Race model.
        """
        # The __str__ method includes both name and date
        expected_str = "Public Race - 07/10/2025"
        actual_str = str(self.public_race)
        self.assertEqual(actual_str, expected_str, 
                        f"Expected '{expected_str}', got '{actual_str}'")

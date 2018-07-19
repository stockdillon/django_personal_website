from django.test import TestCase

# Create your tests here.

class InitialTestCase(TestCase):
    def setUp(self):
        self.var = "Dillon's Value"

    def test_something_worked(self):
        """
        Just making sure I have properly built a Django Framework Test Case
        """
        self.assertEqual("successful assertion","successful assertion")

    def test_two(self):
        self.assertTrue(True)

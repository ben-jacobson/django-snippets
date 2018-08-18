from django.test import TestCase

# Create your tests here.

class smoketest(TestCase):
    def test_fail(self):
        self.fail("complete these tests")
from django.conf import settings
from django.test import TestCase

class BasicTest(TestCase):
    def test_debug_off(self):
        self.assertFalse(settings.DEBUG)
        
    def test_admin_homepage(self):
        r = self.client.get('/', follow=True)
        self.assertEqual(r.status_code, 200)
    

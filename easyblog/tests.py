"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.core.urlresolvers import reverse
from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
        
def get(self, url_name, *args, **kwargs):
    return self.client.get(reverse(url_name,  args=args, kwargs=kwargs))

def post(self, url_name, *args, **kwargs):
    data = kwargs.pop("data", None)
    return self.client.post(reverse(url_name, args=args, kwargs=kwargs), data)

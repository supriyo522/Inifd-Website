from django.test import TestCase
import re

# Create your tests here.

regex = re.compile("^[6-9]\d{9}$")

mobile_number = "5876543210"
print(re.match(regex, mobile_number))
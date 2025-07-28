# test_module1.py
# Purpose: Contains test cases for your modules using the unittest framework (or pytest, if you prefer).

# How to Use:
# - Helps catch bugs early and ensure your code works as expected.
# Run tests using:
# python -m unittest discover tests


# Example Code
import unittest
from my_project.module1 import greet

class TestModule1(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")

if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3

import sys
import unittest

class TestMyCode(unittest.TestCase):

    def test_create_command(self):
        # Test the create command
        result = ("create User")
        self.assertIn("User", result)
        self.assertIn("id", result)

    def test_show_command(self):
        # Test the show command
        result = ("show User 1234")
        self.assertIn("User", result)
        self.assertIn("id", result)
        self.assertIn("1234", result)

    def test_destroy_command(self):
        # Test the destroy command
        result = ("destroy User 1234")
        self.assertIn("Deleted", result)

    def test_all_command(self):
        # Test the all command
        result = ("all User")
        self.assertIn("User", result)
        self.assertIn("id", result)

    def test_update_command(self):
        # Test the update command
        result = ("update User 1234 name John")
        self.assertIn("Updated", result)

if __name__ == '__main__':
    unittest.main()
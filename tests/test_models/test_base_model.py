#!/usr/bin/python3
"""uinttest module"""
import unittest


class Test_Base_model(unittest.TestCase):
    """
    Tests attributes of the base model
    """

    def setUp(self):
        """
        Classes needed for testing
        """
        self.a = 10
        self.b = 20

    def tearDown(self) -> None:
        self.a = None
        self.b = None

    

if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""uinttest module"""
import unittest


class Test_Base_model(unittest.TestCase):

    def setUp(self):
        self.a = 10
        self.b = 20

    def tearDown(self) -> None:
        self.a = None
        self.b = None

    
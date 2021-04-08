import unittest

class TestFunction(unittest.TestCase):
    def setup_class(self):
        print("setup_class called once for the class")

    def teardown_class(self):
        print("teardown_class called once for the class")


    def setup_method(self, _method):
        print("setup_method called for every method")

    def teardown_method(self, _method):
        print("teardown_method called for every method")


    def test_one(self):
        #pass
        self.assertEqual("dummy-value", "dummy-value")

    def test_two(self):
        #false
        self.assertEqual("dummy", "dummy-value")

    def test_three(self):
        print("three")
        assert True
        print("three after")
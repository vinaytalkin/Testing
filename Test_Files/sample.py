import unittest
import ZBase_Framework.Utilities.HtmlTestRunner as results
import HtmlTestRunner

class Example(unittest.TestCase):
    @classmethod
    def setUpClass(class_name):
        print("setUpClass executed it will run only once")
    def setUp(self):
        print("setUp executed when we run each test")
        self.assertEqual(1, 2)
    def test_2(self):
        print("test-1 executed")
    def test_1(self):
        print("test-2 executed")
        self.assertEqual(1, 1)
    def tearDown(self):
        print("tearDown executed when we run each test")
    @classmethod
    def tearDownClass(class_name):
        print("tearDownClass executed it will run only once ")

if __name__ == '__main__':
    res = results.Results()
    res.results()
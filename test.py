import unittest
from hello import *


class Test01_HelloWorld(unittest.TestCase):
    def test_list_int(self):
        result = hello_world()
        self.assertEqual(result, 'Hello World!')


class Test01_HelloName(unittest.TestCase):
    def test_list_int(self):
        result = hello_name('Gabriel')
        self.assertEqual(result, 'Hello Gabriel!')


if __name__ == '__main__':
    with open('test.py', 'w') as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)

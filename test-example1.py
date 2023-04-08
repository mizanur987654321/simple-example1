import unittest
import example1

class TestExample1(unittest.TestCase):
    def test_e1(self):
        result=example1.f1()
        self.assertEqual(result,"Example 1")

if __name__ == '__main__':
    unittest.main()

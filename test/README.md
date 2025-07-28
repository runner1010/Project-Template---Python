unittest Summary (Python's Built-in Testing Framework)
Key Points:
- Part of the standard library (import unittest)
- Uses class-based structure: tests are methods in a subclass of unittest.TestCase
- Uses assert methods like:
    - self.assertEqual(a, b)
    - self.assertTrue(x)
    - self.assertRaises(Exception, func, args...)

Example:
//// math_utils.py ////
def add(a, b):
    return a + b

//// test_math_utils.py ////
import unittest
from math_utils import add

class TestMathUtils(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == '__main__':
    unittest.main()

//// Run test on math_utils.py ////
python -m unittest -s discover
or
python test_math_utils.py
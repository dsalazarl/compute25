# test_compute25.py

import unittest
from compute25 import compute25

class TestCompute25(unittest.TestCase):
    def test_compute25_bad_input(self):
        self.assertEqual(compute25("HOLA"), "SIN SOLUCIÓN")


if __name__ == "__main__":
    unittest.main()
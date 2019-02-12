import unittest

from shrink_name import shrink_name

class ShrinkNameTest(unittest.TestCase):
    def test_no_name_given(self):
        self.assertEqual(shrink_name(), '')

    def test_no_name_given(self):
        self.assertEqual(shrink_name(), '')

    def test_a_name_given(self):
        self.assertEqual(shrink_name("Uncle Bob"), "Uncle Bob")

    def test_another_name_given(self):
        self.assertEqual(shrink_name("Bjarne Stroustrup"), "Bjarne S.")


if __name__ == '__main__':
    unittest.main()
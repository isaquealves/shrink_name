import unittest

from shrink_name import shrink_name

class ShrinkNameTest(unittest.TestCase):
    def test_no_name_given(self):
        self.assertEqual(shrink_name(), '')

    def test_none_given(self):
        self.assertEqual(shrink_name(None), '')

    def test_a_name_given(self):
        self.assertEqual(shrink_name("Uncle Bob"), "Uncle Bob")

    def test_another_name_given(self):
        self.assertEqual(shrink_name("Bjarne Stroustrup"), "Bjarne S.")

    def test_an_other_name_given(self):
        self.assertEqual(shrink_name("Yan Rui Fonseca"), "Yan Rui F.")

    def test_my_full_name_given(self):
        self.assertEqual(shrink_name("Isaque Vieira de Sousa Alves"), "Isaque V.")

    def test_my_first_names_given(self):
        self.assertEqual(shrink_name("Isaque Vieira"), "Isaque Vieira")


if __name__ == '__main__':
    unittest.main()
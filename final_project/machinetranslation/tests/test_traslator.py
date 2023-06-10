"""Module Docstring."""
import unittest
import sys
sys.path.append('../')
import translator

class TestFrenchToEnglish(unittest.TestCase):
    """Class Docstring."""
    def test_french_to_english(self):
        """Function Docstring."""
        self.assertEqual(translator.french_to_english('bonjour le monde'),'hello-world')
        self.assertNotEqual(translator.french_to_english('bonjour le monde'),'thanks')


class TestEnglishToFrench(unittest.TestCase):
    """Class Docstring."""
    def test_english_to_french(self):
        """Function Docstring."""
        self.assertEqual(translator.english_to_french('hello world'), 'Salut, le monde')
        self.assertNotEqual(translator.english_to_french('thank you'), 'bonjour')


if __name__ == '__main__':
    unittest.main()

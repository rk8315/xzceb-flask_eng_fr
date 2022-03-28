import unittest
from translator import english_to_french, french_to_english

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
    def test2(self):
        self.assertEqual(french_to_english("Aujourd'hui est un bon jour"), "Today is a good day")
    def test3(self):
        self.assertIsNone(french_to_english(None))


class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
    def test2(self):
        self.assertEqual(english_to_french("Today is a good day"), "Aujourd'hui est un bon jour")
    def test3(self):
        self.assertIsNone(english_to_french(None))

if __name__ == '__main__':
    unittest.main()
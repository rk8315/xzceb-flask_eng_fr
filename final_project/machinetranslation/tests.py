import unittest
from translator import englishToFrench, frenchToEnglish

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
    def test2(self):
        self.assertEqual(frenchToEnglish("Aujourd'hui est un bon jour"), "Today is a good day")
    def test3(self):
        self.assertIsNone(frenchToEnglish(None))


class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
    def test2(self):
        self.assertEqual(englishToFrench("Today is a good day"), "Aujourd'hui est un bon jour")
    def test3(self):
        self.assertIsNone(englishToFrench(None))

if __name__ == '__main__':
    unittest.main()
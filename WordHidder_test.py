import unittest
from WordHidder import HideWord

class Tests(unittest.TestCase):
    def test_Exists(self):
        word = "programming"
        self.assertIn(word, HideWord(word).lower())
    
    def test_CapitalizationExists(self):
        word = "programming"
        self.assertNotEqual(HideWord(word), HideWord(word).lower())
        self.assertNotEqual(HideWord(word), HideWord(word).upper())

unittest.main()
import unittest
from WordHidder import HideWord

class Tests(unittest.TestCase):
    def test_Exists(self):
        word = "programming"
        self.assertIn(word, HideWord(word).lower())
    
    def test_CapitalizationExists(self):
        word = "programming"
        self.assertEqual(HideWord(word).lower(), HideWord(word).lower())

unittest.main()
import unittest
from WordHidder import HideWord

class Tests(unittest.TestCase):
    def test_Exists(self):
        word = "programming"
        self.assertIn(word, HideWord(word).lower())
    
    def test_CapitalizationExists(self):
        word = "programming"
        hidden_text = HideWord(word)
        self.assertNotEqual(hidden_text, hidden_text.lower())
        self.assertNotEqual(hidden_text, hidden_text.upper())

unittest.main()
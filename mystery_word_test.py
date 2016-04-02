import unittest
from mystery_word import *

# what can I test in my mystery word game?

word = ["bird", "calf", "river", "stream", "kneecap",  "cookbook",
             "language", "sneaker", "algorithm", "integration", "brain"]

class TestMysteryWord(unittest.TestCase):

    def test_easy_word(self):
        self.assertEqual(easy_word(word, right, wrong) ["bird", "calf", "river", "stream", "brain"])


if __name__ == '__main__':
    unittest.main()

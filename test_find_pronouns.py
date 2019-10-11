import unittest
from parser import count_multiple_words, is_retweet

PRONOUNS = ['han', 'hon', 'den', 'denna', 'denne', 'hen']

def expectedResult(han=0, hon=0, den=0, denna=0, denne=0, hen=0):
        return {'han': han, 'hon': hon, 'den': den, 'denna': denna, 'denne': denne, 'hen': hen}

class Testfind_pronouns(unittest.TestCase):
    def test_empty_word_list(self):
        s = "Random string here"
        r = count_multiple_words(s, [])
        self.assertEqual({}, r)
    
    def test_no_pronouns(self):
        s = "Inga pronomer här inte"
        r = count_multiple_words(s, PRONOUNS)
        self.assertEqual(expectedResult(), r)

    def test_han_end(self):
        s = "Inga pronomer här inte, förutom han"
        r = count_multiple_words(s, PRONOUNS)
        self.assertEqual(expectedResult(han=1), r)

    def test_hon_middle(self):
        s = "Inga pronomer förutom hon här inte"
        r = count_multiple_words(s, PRONOUNS)
        self.assertEqual(expectedResult(hon=1), r)

    def test_den_beginig(self):
        s = "den pronomen finns här"
        r = count_multiple_words(s, PRONOUNS)
        self.assertEqual(expectedResult(den=1), r)

    def test_denna(self):
        s = "Inga pronomer här inte, denna räknas"
        r = count_multiple_words(s, PRONOUNS)
        self.assertEqual(expectedResult(denna=1), r)

    def test_denne(self):
        s = "Inga pronomer här inte, denne räknas"
        r = count_multiple_words(s, PRONOUNS)
        self.assertEqual(expectedResult(denne=1), r)

    def test_hen_only(self):
        s = "hen"
        r = count_multiple_words(s, PRONOUNS)
        self.assertEqual(expectedResult(hen=1), r)

    def test_han_capital_letter(self):
        s = "Han är en pronom"
        r = count_multiple_words(s, PRONOUNS)
        self.assertEqual(expectedResult(han=1), r)

    def test_hon_punctuation(self):
        s = "Inga pronomer, förutom hon, här inte"
        r = count_multiple_words(s, PRONOUNS)
        self.assertEqual(expectedResult(hon=1), r)

    def test_den_multiple(self):
        s = "den pronomen finns här den"
        r = count_multiple_words(s, PRONOUNS)
        self.assertEqual(expectedResult(den=2), r)

    def test_denna_only_multiple(self):
        s = "denna denna, denna! denna. denna? Denna"
        r = count_multiple_words(s, PRONOUNS)
        self.assertEqual(expectedResult(denna=6), r)

    def test_escaped_character(self):
        s = "\"BYT HATAR DEN\""
        r = count_multiple_words(s, PRONOUNS)
        self.assertEqual(expectedResult(den=1), r)

    def test_subword_suffix_before_word(self):
        s = "döden den"
        r = count_multiple_words(s, PRONOUNS)
        self.assertEqual(expectedResult(den=1), r)

    def test_subword_prefix_before_word(self):
        s = "hans han"
        r = count_multiple_words(s, PRONOUNS)
        self.assertEqual(expectedResult(han=1), r)

    def test_mix_of_words(self):
        s = "Jag han hon och den det dem hen och så vidare"
        r = count_multiple_words(s, PRONOUNS)
        self.assertEqual(expectedResult(han=1, hon=1, den=1, hen=1), r)

    def test_is_retweet_true(self):
        tweet = {"created_at":"T","id":7,"id_str":"7","text":"V",
            "retweeted_status":{"created_at":"W"}, "retweeted":False}
        self.assertTrue(is_retweet(tweet))

    def test_is_retweet_false(self):
        tweet = {"created_at":"T","id":7,"id_str":"7","text":"V", "retweeted":False}
        self.assertFalse(is_retweet(tweet))



if __name__ == '__main__':
    unittest.main()
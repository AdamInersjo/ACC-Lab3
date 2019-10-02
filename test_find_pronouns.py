import unittest
from parser import find_pronouns

def expectedResult(han=0, hon=0, den=0, denna=0, denne=0, hen=0):
        return {'han': han, 'hon': hon, 'den': den, 'denna': denna, 'denne': denne, 'hen': hen}

class Testfind_pronouns(unittest.TestCase):
    
    def test_no_pronouns(self):
        s = "Inga pronomer här inte"
        r = find_pronouns(s)
        self.assertEqual(expectedResult(), r)

    def test_han_end(self):
        s = "Inga pronomer här inte, förutom han"
        r = find_pronouns(s)
        self.assertEqual(expectedResult(han=1), r)

    def test_hon_middle(self):
        s = "Inga pronomer förutom hon här inte"
        r = find_pronouns(s)
        self.assertEqual(expectedResult(hon=1), r)

    def test_den_beginig(self):
        s = "den pronomen finns här"
        r = find_pronouns(s)
        self.assertEqual(expectedResult(den=1), r)

    def test_denna(self):
        s = "Inga pronomer här inte, denna räknas"
        r = find_pronouns(s)
        self.assertEqual(expectedResult(denna=1), r)

    def test_denne(self):
        s = "Inga pronomer här inte, denne räknas"
        r = find_pronouns(s)
        self.assertEqual(expectedResult(denne=1), r)

    def test_hen_only(self):
        s = "hen"
        r = find_pronouns(s)
        self.assertEqual(expectedResult(hen=1), r)

    def test_han_capital_letter(self):
        s = "Han är en pronom"
        r = find_pronouns(s)
        self.assertEqual(expectedResult(han=1), r)

    def test_hon_punctuation(self):
        s = "Inga pronomer, förutom hon, här inte"
        r = find_pronouns(s)
        self.assertEqual(expectedResult(hon=1), r)

    def test_den_multiple(self):
        s = "den pronomen finns här den"
        r = find_pronouns(s)
        self.assertEqual(expectedResult(den=2), r)

    def test_denna_only_multiple(self):
        s = "denna denna, denna! denna. denna? Denna"
        r = find_pronouns(s)
        self.assertEqual(expectedResult(denna=6), r)

    def test_escaped_character(self):
        s = "\"BYT HATAR DEN\""
        r = find_pronouns(s)
        self.assertEqual(expectedResult(den=1), r)

    def test_subword_suffix_before_word(self):
        s = "döden den"
        r = find_pronouns(s)
        self.assertEqual(expectedResult(den=1), r)

    def test_subword_prefix_before_word(self):
        s = "hans han"
        r = find_pronouns(s)
        self.assertEqual(expectedResult(han=1), r)

    def test_mix_of_words(self):
        s = "Jag han hon och den det dem hen och så vidare"
        r = find_pronouns(s)
        self.assertEqual(expectedResult(han=1, hon=1, den=1, hen=1), r)



if __name__ == '__main__':
    unittest.main()
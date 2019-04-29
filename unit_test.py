import unittest
from get_vowel_num import getCount
from spin_worlds import spin_words
from get_capitals import capitals
from digital_root import digital_root


class TestLeetCodeFunction(unittest.TestCase):

    def test_get_vowel_num(self):
        self.assertEqual(getCount('abracadabra'),5)
        self.assertEqual(getCount('abc'),1)
    
    def test_spin_words(self):
        self.assertEqual(spin_words('Hey fello warriors'), 'Hey ollef sroirraw')
        self.assertEqual(spin_words('This is a test'), 'This is a test')
        self.assertEqual(spin_words('Welcome'), 'emocleW')

    def test_capitals(self):
        self.assertEqual(capitals('CodEWaRs'), [0,3,4,6])
        self.assertEqual(capitals('AbcEfghABCDE'), [0, 3, 7, 8, 9, 10, 11])
        self.assertEqual(capitals('AAAAA'), [0,1,2,3,4])

    def test_digital_root(self):
        self.assertEqual(digital_root(12345), 15)
        self.assertEqual(digital_root(10), 1)
        self.assertEqual(digital_root(11111111), 8)




if __name__ == '__main__':
    unittest.main()
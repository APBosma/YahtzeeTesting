import unittest
from Yahtzee import YahtzeeRoll

class TestYahtzee(unittest.TestCase):
    def setUp(self):
        self.rolls = YahtzeeRoll()
        
    #Upper testing
    def testCounts(self):
        roll = [2, 2, 3, 3, 5]
        upper,lower = self.rolls.score(roll)
        self.assertEqual(lower, 0)
        self.assertEqual(upper, 6)

        
    def testsecondCount(self):
        roll = [5, 5, 3, 1, 1]
        upper,lower = self.rolls.score(roll)
        self.assertEqual(lower, 0)
        self.assertEqual(upper, 10)
        
    #testing three and four
    def testthreeTest(self):
        roll = [5, 5, 5, 2, 1]
        upper,lower = self.rolls.score(roll)
        self.assertEqual(lower, 18)
        self.assertEqual(upper, 15)
        
    def testfourTest(self):
        roll = [6, 6, 6, 6, 5]
        upper,lower = self.rolls.score(roll)
        self.assertEqual(lower, 29)
        self.assertEqual(upper, 24)
        
    #small straight
    def testsmallStraightTest(self):
        roll = [1, 2, 3, 4, 1]
        upper,lower = self.rolls.score(roll)
        self.assertEqual(lower, 30)
        self.assertEqual(upper, 4)
    
    def testsmallStraightTest2(self):
        roll = [2, 3, 4, 5, 5]
        upper,lower = self.rolls.score(roll)
        self.assertEqual(lower, 30)
        self.assertEqual(upper, 10)
        
    #large straight
    def testlargeStraightTest(self):
        roll = [2, 3, 4, 5, 6]
        upper,lower = self.rolls.score(roll)
        self.assertEqual(lower, 40)
        self.assertEqual(upper, 6)
    
    def testlargeStraightTest2(self):
        roll = [2, 3, 4, 5, 1]
        upper,lower = self.rolls.score(roll)
        self.assertEqual(lower, 40)
        self.assertEqual(upper, 5)
        
    #house
    def testHouse(self):
        roll = [2, 2, 2, 4, 4]
        upper,lower = self.rolls.score(roll)
        self.assertEqual(lower, 25)
        self.assertEqual(upper, 8)
        
    def testHouse2(self):
        roll = [1, 1, 1, 3, 3]
        upper,lower = self.rolls.score(roll)
        self.assertEqual(lower, 25)
        self.assertEqual(upper, 6)
        
    
    def testyahtzeeTest(self):
        roll = [1, 1, 1, 1, 1]
        upper,lower = self.rolls.score(roll)
        self.assertEqual(lower, 50)
        self.assertEqual(upper, 5)
      
    
if __name__ == '__main__':
    unittest.main()

import unittest
from Yahtzee import YahtzeeRoll

class TestYahtzee(unittest.TestCase):
    def setUp(self):
        self.rolls = YahtzeeRoll()
        
    #Upper testing
    def testCounts(self):
        roll = [2, 2, 3, 3, 5]
        upper,lower = self.rolls.score(roll)
        self.assertEqual(self.rolls.score(roll), "Highest possible upper score: 6\nHighest possible lower score: 0")
    '''    
    def testsecondCount(self):
        roll = [5, 5, 3, 1, 1]
        self.assertEqual(self.rolls.score(roll),15)
        
    #testing three and four
    def testthreeTest(self):
        roll = [5, 5, 5, 2, 1]
        self.assertEqual(self.rolls.score(roll), 18)
        
    def testfourTest(self):
        roll = [6, 6, 6, 6, 5]
        self.assertEqual(self.rolls.score(roll), 29)
        
    #small straight
    def testsmallStraightTest(self):
        roll = [1, 2, 3, 4, 1]
        self.assertEqual(self.rolls.score(roll), 30)
    
    def testsmallStraightTest2(self):
        roll = [2, 3, 4, 5, 5]
        self.assertEqual(self.rolls.score(roll), 30)
        
    #large straight
    def testlargeStraightTest(self):
        roll = [2, 3, 4, 5, 6]
        self.assertEqual(self.rolls.score(roll), 40)
    
    def testlargeStraightTest2(self):
        roll = [2, 3, 4, 5, 1]
        self.assertEqual(self.rolls.score(roll), 40)
        
    #house
    def testHouse(self):
        roll = [2, 2, 2, 4, 4]
        self.assertEqual(self.rolls.score(roll), 25)
        
    def testHouse2(self):
        roll = [1, 1, 1, 3, 3]
        self.assertEqual(self.rolls.score(roll), 25)
        
    def testyahtzeeTest(self):
        roll = [1, 1, 1, 1, 1]
        self.assertEqual(self.rolls.score(roll), 50)
      '''  
    
if __name__ == '__main__':
    unittest.main()

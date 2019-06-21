import unittest
from chips import Chips

class ChipsTest(unittest.TestCase):
    
    def test_chips_values(self):
        #Make sure negative value errors are raised 
        test_chips = Chips()
        test_chips.bet = -1
        test_chips.total = 100
        
        
        self.assertRaises(ValueError, Chips.take_bet, test_chips)

    def test_chips_types(self):
        #Make sure type errors are raised
        test_chips_values = Chips()
        test_chips_values.bet = 'hey'
        test_chips_values.total = 'waht'

        self.assertRaises(TypeError, Chips.take_bet, test_chips_values)

if __name__ == '__main__':
    unittest.main()
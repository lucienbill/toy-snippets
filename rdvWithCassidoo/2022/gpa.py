import math

def calculateGPA(grades):
    notes = {
        "A":4,
        "A-":3.7,
        "B+":3.3,
        "B":3,
        "B-":2.7,
        "C+":2.3,
        "C":2,
        "C-":1.7,
        "D+":1.3,
        "D":1,
        "D-":0.7,
        "F":0
    }
    
    result = sum(notes[g] for g in grades)/len(grades)
    # round the result... but not with round(), because round(2.25) = 2.2
    # (and I need it to equal 2.3).
    # See https://realpython.com/python-rounding/
    def round_half_up(n, decimals=0):
        multiplier = 10 ** decimals
        return math.floor(n*multiplier + 0.5) / multiplier
    
    return round_half_up(result, 1)

### UNIT TEST ###
# Note: this entire code was tested on https://www.online-python.com/
import unittest
class HappyPath(unittest.TestCase):

    def test_one_grade(self):
        self.assertEqual(calculateGPA(['A']), 4)

    def test_allF(self):
        self.assertEqual(calculateGPA(['F', 'F', 'F']), 0)

    def test_grades_with_modifiers_1(self):
        self.assertEqual(calculateGPA(['A', 'A-', 'B+', 'B', 'B-']), 3.3)
        
    def test_grades_with_modifiers_2(self):
        self.assertEqual(calculateGPA(['A', 'B+', 'C-', 'A']), 3.3)
        
class WrongInput(unittest.TestCase):
    def test_unreferrenced_grade(self):
        with self.assertRaises(KeyError):
            calculateGPA(['A', 'B+', 'C-', 'E'])
            
    def test_direct_number(self):
        with self.assertRaises(KeyError):
            calculateGPA(['A', 'B+', 'C-', '3'])
            
class LetsGetSilly(unittest.TestCase):    
    def test_unreferrenced_modifier(self):
        with self.assertRaises(KeyError):
            calculateGPA(['A', 'B+', 'C-', 'C#'])
            
    def test_grade_too_long(self):
        with self.assertRaises(KeyError):
            calculateGPA(['A', 'B+', 'C-', 'DAD'])
            
    def test_the_cheater(self):
        with self.assertRaises(KeyError):
            calculateGPA(['A', 'B+', 'C-', 'I give u $50 for a C'])
            
    def test_helpMeItsMonday(self):
        with self.assertRaises(KeyError):
            calculateGPA(['Never','gonna','give','you','up'])

if __name__ == '__main__':
    unittest.main()

def ordinal(n: int) -> str:
    # What is an ordinal? See https://www.woodwardenglish.com/lesson/ordinal-numbers-in-english/
    if type(n) != type(1):
        raise TypeError("the value given to ordinal must be a positive integer")
    
    r = f'{n}'
    last_digits = int(r[-2:])
    last_digit = int(r[-1])
    
    # last 2 digits: x1, x2, x3 -> st, nd, rd ; unless x == 1
    if last_digits not in set([11, 12, 13]):
        if last_digit == 1:
            r += "st"
        elif last_digit == 2:
            r += "nd"
        elif last_digit == 3:
            r += "rd"
        else:
            r += "th"
    else:
        r += "th"
    
    return r

# Unit Tests ; can run on https://www.online-python.com/
if __name__ == '__main__':
    import unittest
    
    class TestOrdinalSingleDigit(unittest.TestCase):
        def test_1(self):
            self.assertEqual(ordinal(1), "1st")
            
        def test_2(self):
            self.assertEqual(ordinal(2), "2nd")
    
        def test_3(self):
            self.assertEqual(ordinal(3), "3rd")
    
        def test_4(self):
            self.assertEqual(ordinal(4), "4th")
    
        def test_5(self):
            self.assertEqual(ordinal(5), "5th")
    
        def test_6(self):
            self.assertEqual(ordinal(6), "6th")
    
        def test_7(self):
            self.assertEqual(ordinal(7), "7th")
    
        def test_8(self):
            self.assertEqual(ordinal(8), "8th")
    
        def test_9(self):
            self.assertEqual(ordinal(9), "9th")
    
        def test_0(self):
            self.assertEqual(ordinal(0), "0th")
    
    class TestOrdinalTens(unittest.TestCase):
        def test_10(self):
            self.assertEqual(ordinal(10), "10th")
            
        def test_11(self):
            self.assertEqual(ordinal(11), "11th")
    
        def test_12(self):
            self.assertEqual(ordinal(12), "12th")
    
        def test_13(self):
            self.assertEqual(ordinal(13), "13th")
    
        def test_14(self):
            self.assertEqual(ordinal(14), "14th")
    
    class TestOrdinalTwoDigits(unittest.TestCase):
        def test_20(self):
            self.assertEqual(ordinal(20), "20th")
            
        def test_21(self):
            self.assertEqual(ordinal(21), "21st")
            
        def test_22(self):
            self.assertEqual(ordinal(22), "22nd")
    
        def test_23(self):
            self.assertEqual(ordinal(23), "23rd")
    
        def test_51(self):
            self.assertEqual(ordinal(51), "51st")
            
        def test_62(self):
            self.assertEqual(ordinal(62), "62nd")
    
        def test_73(self):
            self.assertEqual(ordinal(73), "73rd")
    
    class TestOrdinalMoreDigits(unittest.TestCase):
        def test_173(self):
            self.assertEqual(ordinal(173), "173rd")
        
        def test_44692(self):
            self.assertEqual(ordinal(44692), "44692nd")
        
        def test_14111(self):
            self.assertEqual(ordinal(14111), "14111th")
        
        def test_14131(self):
            self.assertEqual(ordinal(14131), "14131st")
    
    class TestOrdinalError(unittest.TestCase):
        def test_string(self):
            with self.assertRaises(TypeError):
                ordinal("1")
                
        def test_negative(self):
            with self.assertRaises(TypeError):
                ordinal(-1)
                
        def test_float(self):
            with self.assertRaises(TypeError):
                ordinal(3.14)
    
        unittest.main()

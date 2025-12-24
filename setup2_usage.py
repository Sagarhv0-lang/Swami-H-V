import unittest 

class TestMath(unittest.TestCase): 
    counter = 0   
    def setUp(self): 
        self.a = 12
        self.b = 10 
    def tearDown(self):    
        TestMath.counter += 1
        print(f"Completed test {TestMath.counter}") 
    def test_addition(self): 
        self.assertEqual(self.a + self.b, 22)  
    def test_subtraction(self): 
        self.assertEqual(self.a - self.b, 2)   
    def test_multiplication(self): 
        self.assertEqual(self.a * self.b, 120)  
    def test_division(self): 
        self.assertEqual(self.a / self.b, 1.2)  

if __name__ == "__main__": 
    unittest.main()

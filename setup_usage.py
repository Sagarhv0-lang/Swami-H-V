import unittest 

class TestMath(unittest.TestCase): 
    def setUp(self): 
        self.a = 10 
        self.b = 5 

    def tearDown(self): 
        print("Test completed") 

    def test_addition(self): 
        self.assertEqual(self.a + self.b, 15) 

    def test_subtraction(self): 
        self.assertEqual(self.a - self.b, 5) 

if __name__ == "__main__": 
    unittest.main()

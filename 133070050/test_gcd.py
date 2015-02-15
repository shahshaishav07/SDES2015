from gcd import gcd

#def test_gcd ():
  #assert gcd (1,1) == 1
  #assert gcd (1,89) == 1
  #assert gcd (0,72637) == 72637
  #assert gcd (77,88) == 11
#  assert gcd (-1,9)
#  gcd ("ll",9)


import unittest
class TestGcdFunction(unittest.TestCase):
  def setUp(self):
    # Called before each test case.
    print "In setUp"
  def tearDown(self):
    print "In tearDown"

  def test_gcd(self):
    self.assertEqual(gcd(45, 5), 5)
    self.assertEqual(gcd(1, 1), 1)
    self.assertEqual(gcd(0, 901), 901)
    self.assertEqual(gcd(77, 88), 11)
    
  def test_gcd_exception(self):
    self.assertRaises(ValueError, gcd(11, -22))  
    self.assertRaises(ValueError, gcd(-100, -422))  
    self.assertRaises(ValueError, gcd(-89, 2))  
    self.assertRaises(TypeError, gcd("0l", 4))  
    self.assertRaises(TypeError, gcd("number", "number2"))  
    self.assertRaises(TypeError, gcd(90,"4"))  

  
if __name__ == '__main__':
  unittest.main()
  #test_gcd ()
  

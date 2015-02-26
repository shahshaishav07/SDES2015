from text_plot import plot



import unittest


class TestPlotFunction(unittest.TestCase):
  def setUp(self):
    # Called before each test case.
    print "In setUp"
  def tearDown(self):
    print "In tearDown"


  def test_plot(self):
# Test 1: Just plots simple function (linear)    
    x = [1,2,3,4,5]
    y = [1,2,3,4,5]
    plot_1=plot(x, y, size=(10,10))
# Test 1 (contd.) : Modifies that plot size and replots that function    
    plot_1.size=(35,35)
    print plot_1
    


# Test 2: Plot of Sinusidal Function   
    import numpy as np
    x = np.linspace(0, 2*np.pi, 40)
    plot_2=plot (x, np.sin(x), size=(20, 60))
    plot_2.size= (40,110)
    print plot_2
    
# Test 3: Plot of Exponential Function   
    import numpy as np
    x = np.linspace(0, 3, 40)
    plot_2=plot (x, np.exp(x), size=(20, 60))
    plot_2.size= (25,55)
    print plot_2
  
  def test_plot_exception(self):

# Test 4: Check for Exception: If array is mismatched, exception should be raised.

    self.assertRaises(Exception, plot([1,2,3,4,5],[7,9,10,11]))  
    
  
if __name__ == '__main__':
  unittest.main()
  #test_gcd ()
  

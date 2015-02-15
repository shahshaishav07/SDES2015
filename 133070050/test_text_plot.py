import text_plot

def test_convert_tupple_to_int (x,y,terminal_col,terminal_row,x_i,y_i):
  assert text_plot.convert_tupple_to_int (x,y,terminal_col, terminal_row) == x_i,y_i 
  
  
def test_matrix_calculation (x_i,y_i,terminal_col,terminal_row,matrix):
  assert text_plot.matrix_calculation (x_i,y_i,terminal_col,terminal_row) == matrix
  
def test_plot (x,y):
  text_plot.plot (x,y)

if __name__=='__main__':
  x= (0.0, 0.314, 0.628, 0.942, 1.256, 1.570, 1.884, 2.199, 2.513, 2.827, 3.141, 3.455, 3.769, 4.084, 4.398, 4.71, 5.026, 5.340, 5.654, 5.969)
  y= (0.0, 0.309, 0.587, 0.809, 0.951, 1.0, 0.951, 0.809, 0.587, 0.309, 1.2246467991473532e-16, -0.309, -0.587, -0.809, -0.951, -1.0, -0.951, -0.809, -0.587, -0.309)
  
  x_i= [1, 6, 13, 20, 27, 34, 41, 48, 55, 62, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133]
  y_i= [20, 26, 32, 36, 39, 40, 39, 36, 32, 26, 20, 13, 7, 3, 0, 1, 0, 3, 7, 13]

  # Test_1 full screen view for sine
#  test_convert_tupple_to_int (x,y,134,41,x_i,y_i)
  test_plot (x,y)

  #Test 2 Full screen View for cosine
  x=[]
  y=[]
  import math
  x_length= (math.pi)*2
  nos_of_points= 50
  interval = x_length/nos_of_points
  
  for i in range (0,nos_of_points):
    x.append(i*interval)
    y.append(math.cos (x[i]))
#  print x
#  print sin_x
  test_plot (tuple (x), tuple (y))







  #Test 3 Full screen View for exp
  
  x=[]
  y=[]
  x_length= (math.pi)*2
  nos_of_points= 25
  interval = x_length/nos_of_points
  
  for i in range (0,nos_of_points):
    x.append(i*interval)
    y.append(math.exp (x[i]))
#  print x
#  print sin_x
  test_plot (tuple (x), tuple (y))
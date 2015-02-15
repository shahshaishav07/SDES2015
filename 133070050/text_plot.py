def plot (x,y):
  import os
  terminal_row, terminal_col =os.popen('stty size','r').read().split()
  terminal_row = int (terminal_row)
  terminal_col= int (terminal_col)
#  print terminal_col, terminal_row
  x_i, y_i = convert_tupple_to_int (x,y,terminal_col,terminal_row)
  matrix=matrix_calculation (x_i,y_i,terminal_col,terminal_row)
  print_plot (matrix)
  return x_i,y_i






# Function which converts floats into scaled integer 
# in the range of console (width, height)
def convert_tupple_to_int (x,y,x_terminal, y_terminal):
  x_length = len (x)  
  y_length = len (y)
  x_max = max (x)
  y_max = max (y)
  x_min = min (x)
  y_min = min (y)
  x_range = x_max-x_min
  y_range = y_max-y_min
  x_abs = []
  y_abs = []
  
  if (x_min <0):
    for i in range (0,x_length):
      x_abs.append (x[i]  - x_min)
  else:
    for i in range (0,x_length):
      x_abs.append (x[i])
 
  if (y_min <0):
    for i in range (0,y_length):
      y_abs.append (y[i]  - y_min)
  else:
    for i in range (0,y_length):
      y_abs.append (y[i])
  x_i = []
  y_i = []
  min_len = min (x_length, y_length)
#  print x_length, y_length, x_max, y_max
  x_max = max (x_abs)
  y_max = max (y_abs)
  for i in range (0,min_len):
    a= abs(int(round(((x_abs[i])*x_terminal)/x_max)-1))
    if a not in x_i:
      x_i.append (a)
      y_i.append (abs(int(round(((y_abs[i])*y_terminal)/y_max)-1)))
#    print x_i, y_i
#  print x,y,x_terminal, y_terminal
#  print x_i, y_i
  return x_i, y_i

#abs(int((math.sin(mathth.pi/2)-math.sin(math.pi))/))



# Function to check the availability of the corresponding co-ordinate
def matrix_calculation (x_i,y_i,terminal_col,terminal_row):
#  matrix =[[0]*terminal_col]*terminal_row
  matrix =[[0 for x in range(terminal_col)] for x in range(terminal_row)]
  x_length = len (x_i)
  y_length = len (y_i)
  min_len = min (x_length,y_length)
#  print matrix
  for i in range (0,min_len):
    matrix [(y_i[i])][(x_i[i])] = 1
#  print matrix
  return matrix


# Function to print '*' at appropriate co-ordinate.

def print_plot (matrix):
  from sys import stdout
  no_of_rows = len (matrix)
#  print no_of_rows
  for i in range (no_of_rows-1,0,-1):
    stdout.write ('\n')
    no_of_col = len (matrix[i])
    for j in range (0, no_of_col):
      if (matrix [i][j]== 1):
	stdout.write ('*')
      else:
	stdout.write (' ')
	

if __name__ == '__main__':
  #x= (0.1,0.2,0.3,0.4,0.5)
  #y= (1,2,3,4,5)
  #plot (x,y)
  
  x=[]
  sin_x=[]
  import math
  x_length= (math.pi)*2
  nos_of_points= 30
  interval = x_length/nos_of_points
  
  for i in range (0,nos_of_points):
    x.append(i*interval)
    sin_x.append(math.sin (x[i]))
#  print x
#  print sin_x
  plot (tuple (x), tuple (sin_x))
  


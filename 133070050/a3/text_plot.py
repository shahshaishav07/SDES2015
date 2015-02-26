

# Defination of class plot
class plot ():
  
# Initialization block which initializes all the blocks whenever
# plot (x,y) is entered.

# Member Functions are called in an appropriate order

  def __init__ (self,x_sequence, y_sequence, size = (30,80)):
    self.x=x_sequence
    self.y=y_sequence
    self.size=size
    
    try:
      if len(self.x) != len(self.y):
	raise Exception
    except Exception:
      print "Input arrays have different lengths."
    
    else:
      self.xmin, self.xmax = min(self.x), max(self.x)
      self.ymin, self.ymax = min(self.y), max(self.y)
      
      self.canvas = self.make_canvas ()
      for i in range(len(self.x)):
	  self.x_element, self.y_element = self.x[i], self.y[i]
	  xi, yi = self.map_point()
	  self.canvas[yi][xi] = '*'
      
    
      self.result_string=self.plot_canvas ()
      print self.result_string
      
    

# whenever any parameter of plot is changed, it will reproduce 
#the new plot

  def __repr__ (self):
    
    
    try:
      if len(self.x) != len(self.y):
	raise Exception
    except Exception:
      print "Input arrays have different lengths."
    
    else:
      
      self.xmin, self.xmax = min(self.x), max(self.x)
      self.ymin, self.ymax = min(self.y), max(self.y)
      
      self.canvas = self.make_canvas ()
      for i in range(len(self.x)):
	  self.x_element, self.y_element = self.x[i], self.y[i]
	  xi, yi = self.map_point()
	  self.canvas[yi][xi] = '*'
      
    
      self.result_string=self.plot_canvas ()
      return self.result_string
    




# Makes canvas of the specified size

  def make_canvas (self):
    self.cols, self.rows = self.size [0], self.size[1]
    canvas = []
    for i in range(0, self.cols):
        canvas.append(list(' '*self.rows))
    return canvas


  def map_point (self):
    """Return a pair of indices corresponding to
    the point x, y in the domain (xmin,...)
    """
    len_x = float(self.xmax - self.xmin)
    len_y = float(self.ymax - self.ymin)
    self.xpoint = int(round((self.x_element - self.xmin)/len_x*(self.size[1]-1)))
    self.ypoint = int(round((self.y_element - self.ymin)/len_y*(self.size[0]-1)))
    return self.xpoint,self.ypoint
    
  def plot_canvas (self):
    self.rslt_str_list=[]
    for line in self.canvas[::-1]:
        self.rslt_str_list.append(''.join(line))
    self.rslt_str = '\n'.join(self.rslt_str_list)
    return self.rslt_str;
    




# When this script will run, it will produce sine plot     
if __name__ == '__main__':
    import numpy as np
    x = np.linspace(0, 2*np.pi, 50)
    plot (x, np.sin(x), size=(30, 80))

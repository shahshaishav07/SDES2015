def gcd (a,b):
  
  try :
    if ((type(a) == int or type (a) == long) and (type (b) == int or type (b)== long)):
      if (a<0 or b<0):
	raise ValueError
    else:
      raise TypeError
  except TypeError:
    print "TypeError Exception: Arguments are not of Integer type"
  except ValueError:
    print "ValueError Exception: Argument is negative. It must be positive"
  
  else:
    while b:
      a,b = b, a%b
    return a
      

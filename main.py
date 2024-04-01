from datetime import datetime
from sys import orig_argv
import time


# Part 1
def clock(n):
    # Your code here
    """
    Clock format: hh:mm:ss
    Show time and update once every second
  
    """
    interval = 0
    time_now = datetime.now()
    time_now = time_now.strftime('%H:%M:%S')
    while (interval < n):
      print(time_now, end = '\r')
      time.sleep(1)
      interval += 1

# Part 2
def lcm(a, b):
    # Your code here
    """
    return lowest common multiple of 2 integers
    
    """
    a_original = a
    b_original = b
    while(a != b):
      if a < b:
        a = a + a_original
      elif b < a:
        b = b + b_original
      else:
        break
      
    return a


# Part 3
def gcf(a, b):
    # Your code here
    """
    Return the value of greatest common factor of two integers
    gcf(a, b) = gcf(a - b, b) given a > b
    """
    while (a != b):
      if a > b:
        a = a - b
      elif a < b:
        b = b - a
      else:
        break
    return a

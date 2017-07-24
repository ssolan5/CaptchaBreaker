#!/usr/bin/env python

#!/bin/python
import sys

def computeCDF(input):
   dict={}
   count=0
 
   while (1):
      line = input.readline()

      # ignore empty lines
      if not line.strip():
         break

      val = float(line)
      if not (val in dict):
         dict[val]=1
      else:
         dict[val] = dict[val]+1
      count = count + 1
 
   ks = sorted(dict.keys())
   n = 0

   first_value = True

   for k in ks:

      if first_value:
         # patch the valuse for zero
         print "%f 0.0" % k
         first_value = False

      n = n + dict[k]
      print "%f %f" % (k,float(n)/count)
 
if __name__ == '__main__':

   if len(sys.argv) != 2:
      print "\n\tUSAGE:\n\t\tpython %s <data file>\n" % sys.argv[0]
      sys.exit(0)

   input = open(sys.argv[1], "r")

   computeCDF(input)

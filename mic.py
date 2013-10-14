#!/usr/bin/python
import numpy
from scipy import misc

image = numpy.ndarray(shape=(480,640), dtype=float, order='F')
for y in xrange(480):
  for x in xrange(640):
    image[y][x] = (1-(((320-x)**2+(240-y)**2)**.5)/400)*255
misc.imsave('output.png', image)

class source:
  __init__(name, position, direction, type):
    self.name = name
    self.position = position
    self.direction = direction 
    self.type = type

class sink:
  __init__(name, position, direction, type):
    self.name = name
    self.position = position
    self.direction = direction 
    self.type = type

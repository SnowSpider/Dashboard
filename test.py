#!/usr/bin/env python

from odf.opendocument import load
from odf.table import Table

class A:
    def __init__(self, a = 5):
        self.a = a

    def f1(self):
        self.a += 10


class B(A):
    def __init__(self, b = 0):
        A.__init__(self, 4)
        self.b = b

    def f1(self):
        self.b += 10

x = B()
x.f1()
print(x.a,'-', x.b)


class Point: 
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def distance(self):
        return sqrt( (x1-x2)**2 + (y1-y2)**2 + (z1 -z2)**2 )
    
    
p1 = Point(4, 2, 9)

print(p1)




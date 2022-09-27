
''''query-1'''
# Python If-Else

# Task 
# Given an integer, n, perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

# Input Format
# A single line containing a positive integer, n.

# Constraints
# 1 <= n <= 100

# Output Format
# Print Weird if the number is weird; otherwise, print Not Weird.

'''solution'''

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input().strip())
    if N % 2 != 0:
        print("Weird")
    else:
        if N >= 2 and N <= 5:
            print("Not Weird")
        elif N >= 6 and N <= 20:
            print("Weird")
        elif N > 20:
            print("Not Weird")
            
'''----------------end---------------'''

'''query-2'''
In the Gregorian calendar, three conditions are used to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years

'''task'''
Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True   
    # Write your logic here
    
    return leap

year = int(input())
print(is_leap(year))

'''query-3'''
task: print n integers consecutively given n

'''solution'''
import math
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i + 1, end="")
        
'''query-4'''
your task is to print a palindromic triangle of size N.

'''solution'''
for i in range(1, int(input())+1):
    print(int((((10)**i-1)/ 9)**2))
    
'''query-5'''
your task is to print a trianle with sequence of numbers of N
for i in range(5):
    print(int((10**(i+2) - 10 - 9*(i+1))/81))
    
 output:
 N=5
1
12
123
1234
12345

'''query-5'''
your task is to print a numerical traingle of height N-1
for i in range(1, int(input())):
    print(int(i * 10**i/9))
    
output:
N=5
1
22
333
4444

'''query-6'''
Dealing with complex numbers solution in python
import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        r = self.real * no.real - self.imaginary * no.imaginary
        i = self.real * no.imaginary + self.imaginary * no.real
        return Complex(r, i)

    def __truediv__(self, no):
        d = no.real ** 2 + no.imaginary ** 2
        n = self * Complex(no.real, -1 * no.imaginary)
        return Complex(n.real / d, n.imaginary / d)

    def mod(self):
        d = self.real ** 2 + self.imaginary ** 2
        return Complex(math.sqrt(d), 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result
    
        

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')

    
 '''query-7'''
  find the torsional angle problem You are given four points A, B, C, and D in a 3-dimensional Cartesian coordinate system. 
  You are required to print the angle between the plane made by the points A, B, C and B, C, D in degrees
 
 import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        return Points((self.x - no.x), (self.y - no.y), (self.z - no.z))

    def dot(self, no):
        return (self.x * no.x) + (self.y * no.y) + (self.z * no.z)

    def cross(self, no):
        return Points((self.y*no.z - no.y*self.z), (-self.x*no.z + self.z*no.x), (self.x*no.y - self.y*no.x))

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)
    
        
if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
 





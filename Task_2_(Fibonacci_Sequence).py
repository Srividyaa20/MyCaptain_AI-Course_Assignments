# -*- coding: utf-8 -*-
"""TASK - 2 (Fibonacci Sequence).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pcyMBfJB1Lf-HaHDi3dqTR40TYOVpoaY
"""

def Fibonacci(n):
  if n <= 1:
    return n
  else:
    return(Fibonacci(n-1) + Fibonacci(n-2))
nterms = int(input("Enter the no Sequence?"))
if nterms <= 0:
   print("Enter a positive Integer")
else:
   print("Fibonacci sequence: ")
   for i in range(nterms):
    print(Fibonacci(i))
# -*- coding: utf-8 -*-
"""checkpointfiles.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Hw3rgT11ldkjAabC2I-V1Wvv_feFb0aP
"""

#ex1
f = open("python.txt")

#ex2
f = open("python.txt",'r',encoding = 'utf-8')
print(f.readline())

#ex3
for line in f:
       print(line, end = '')

#ex4
f = open("python.txt",'r',encoding = 'utf-8')
data=f.read()
words = data.split()
print(words)
print(len(words))
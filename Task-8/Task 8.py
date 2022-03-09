#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Ques 1
from numpy import *
a=array([])
f=int(input('First Number:'))
l=int(input('Last Number:'))
for i in range(f,l):
    a=append(a,i)
    for i in range(5):
        a=append(a,0)
a=append(a,l)
print(a)


# In[4]:

#Ques 2
from numpy import *
while True:
    a = array([])
    n = int(input("Enter the number of elements in 1st array:"))
    for i in range(n):
        e = int(input("Element:  "))
        a = append(a, e)
    b = array([])
    m = int(input("Enter the number of elements in 2nd array:"))
    for i in range(m):
        f = int(input("Element:  "))
        b = append(b, f)
    print("First Array:",a)
    print("Second Array:",b)
    c=a==b
    e=c.all()
    print(e)
    r=input("Do you want to check one more time(y/n)?")
    if r=='y':
        True
    if r=='n':
        break


# In[5]:

#Ques 3
import numpy as np
print(0 * np.nan)
print(np.nan != np.nan)
print(np.inf > np.nan)
print(np.nan - np.nan)
print(0.3 == 3 * 0.1)


# In[6]:

#Ques 4
import pandas as pd
ser = pd.Series(['amrita', 'school', 'of', 'engineering', 'chennai' , 'campus'])
s=ser.str.capitalize()
for i in s:
    print(i,end=' ')


# In[7]:

#Ques 5
from numpy import *
a = array([])
n = int(input("Enter the number of elements in 1st array:"))
for i in range(n):
    e = int(input("Element:  "))
    a = append(a, e)
b = array([])
m = int(input("Enter the number of elements in 2nd array:"))
for i in range(m):
    f = int(input("Element:"))
    b = append(b, f)
print("First Array:",a)
print("Second Array:",b)
c=a+b
print("The sum of two arrays:",c)
d = int(input("Enter the dimension of I:"))
i = identity(d, dtype="int")
print("The identity matrix of order",d,"is:")
print(i)







